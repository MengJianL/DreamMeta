/**
 * dreammeta-runtime — MCP Server for Meta-Department (元部门)
 *
 * Exposes the 13-atom architecture assets via Model Context Protocol:
 *   Resources: architecture-index, meta-command
 *   Tools:     list_atoms, get_atom
 *
 * Transport: stdio (local process communication)
 * Usage:     node scripts/mcp/dreammeta-runtime.mjs
 * Self-test: node scripts/mcp/dreammeta-runtime.mjs --self-test
 */

import { promises as fs } from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ---------------------------------------------------------------------------
// Paths
// ---------------------------------------------------------------------------

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "../..");
const agentsDir = path.join(repoRoot, ".claude", "agents");
const commandsDir = path.join(repoRoot, ".claude", "commands");

// ---------------------------------------------------------------------------
// Layer mapping — 三层引力结构
// ---------------------------------------------------------------------------

const LAYER_MAP = {
  M01: { layer: "L1", label: "Foundation / 基础层" },
  M02: { layer: "L1", label: "Foundation / 基础层" },
  M03: { layer: "L1", label: "Foundation / 基础层" },
  M04: { layer: "L2", label: "Orchestration / 编排层" },
  M05: { layer: "L2", label: "Orchestration / 编排层" },
  M06: { layer: "L2", label: "Orchestration / 编排层" },
  M07: { layer: "L2", label: "Orchestration / 编排层" },
  M08: { layer: "L2", label: "Orchestration / 编排层" },
  M09: { layer: "L3", label: "Execution / 执行层" },
  M10: { layer: "L3", label: "Execution / 执行层" },
  M11: { layer: "L3", label: "Execution / 执行层" },
  M12: { layer: "L3", label: "Execution / 执行层" },
  M13: { layer: "L3", label: "Execution / 执行层" },
};

// ---------------------------------------------------------------------------
// File loading helpers
// ---------------------------------------------------------------------------

async function readFileSafe(filePath) {
  try {
    return await fs.readFile(filePath, "utf-8");
  } catch {
    return null;
  }
}

/**
 * Parse an atom .md file to extract structured metadata.
 * Atom files use markdown headings (not YAML frontmatter):
 *   # M##-name          → id + name
 *   ## Layer             → layer info (also derived from LAYER_MAP)
 *   ## Identity / 身份定位 → role description
 *   ## Core Function / 核心功能 → core function description
 */
function parseAtom(filename, content) {
  const match = filename.match(/^(M\d{2})-(.+)\.md$/);
  if (!match) return null;

  const id = match[1];
  const name = match[2];
  const layerInfo = LAYER_MAP[id] || { layer: "?", label: "Unknown" };

  // Extract the Identity section for a short role description
  const identityMatch = content.match(
    /## Identity\s*\/?\s*身份定位\s*\n+([\s\S]*?)(?=\n---|\n## )/
  );
  const identityText = identityMatch ? identityMatch[1].trim() : "";

  // Extract the first meaningful sentence as the core responsibility
  const firstSentence = identityText
    .split(/\n/)
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("-") && !l.startsWith("*"))
    .slice(0, 2)
    .join(" ");

  return {
    id,
    name,
    filename,
    layer: layerInfo.layer,
    layerLabel: layerInfo.label,
    coreResponsibility: firstSentence || `Atom ${id}-${name}`,
    fullContent: content,
  };
}

// ---------------------------------------------------------------------------
// Preload all assets into memory at startup
// ---------------------------------------------------------------------------

let architectureIndex = null; // .claude/agents/CLAUDE.md
let metaCommand = null; // .claude/commands/meta.md
let atoms = []; // parsed atom objects, sorted M01..M13
let atomMap = new Map(); // id -> atom

async function preloadAssets() {
  // Load static resources
  architectureIndex = await readFileSafe(
    path.join(agentsDir, "CLAUDE.md")
  );
  metaCommand = await readFileSafe(
    path.join(commandsDir, "meta.md")
  );

  // Discover and load atom files
  let entries;
  try {
    entries = await fs.readdir(agentsDir);
  } catch {
    entries = [];
  }

  const atomFiles = entries
    .filter((f) => /^M\d{2}-.+\.md$/.test(f))
    .sort(); // alphabetical = M01..M13

  for (const file of atomFiles) {
    const content = await readFileSafe(path.join(agentsDir, file));
    if (content === null) continue;
    const atom = parseAtom(file, content);
    if (atom) {
      atoms.push(atom);
      atomMap.set(atom.id, atom);
    }
  }
}

// ---------------------------------------------------------------------------
// Self-test mode: --self-test
// ---------------------------------------------------------------------------

async function selfTest() {
  await preloadAssets();

  const result = {
    ok: true,
    server: "dreammeta-runtime",
    version: "1.0.0",
    resources: {
      count: 0,
      list: [],
    },
    tools: {
      count: 2,
      list: ["list_atoms", "get_atom"],
    },
    atoms: {
      count: atoms.length,
      expected: 13,
      list: atoms.map((a) => `${a.id}-${a.name}`),
    },
    issues: [],
  };

  // Check resources
  if (architectureIndex) {
    result.resources.count++;
    result.resources.list.push("dreammeta://architecture-index");
  } else {
    result.issues.push("MISSING: .claude/agents/CLAUDE.md");
  }

  if (metaCommand) {
    result.resources.count++;
    result.resources.list.push("dreammeta://meta-command");
  } else {
    result.issues.push("MISSING: .claude/commands/meta.md");
  }

  // Check atoms
  if (atoms.length !== 13) {
    result.issues.push(
      `Expected 13 atoms, found ${atoms.length}`
    );
  }

  // Verify all M01-M13 present
  for (let i = 1; i <= 13; i++) {
    const id = `M${String(i).padStart(2, "0")}`;
    if (!atomMap.has(id)) {
      result.issues.push(`MISSING atom: ${id}`);
    }
  }

  if (result.issues.length > 0) {
    result.ok = false;
  }

  console.log(JSON.stringify(result, null, 2));
  process.exit(result.ok ? 0 : 1);
}

// ---------------------------------------------------------------------------
// Main: register MCP resources and tools, then connect
// ---------------------------------------------------------------------------

async function main() {
  // Handle --self-test before anything else
  if (process.argv.includes("--self-test")) {
    await selfTest();
    return;
  }

  await preloadAssets();

  const server = new McpServer({
    name: "dreammeta-runtime",
    version: "1.0.0",
  });

  // ----- Resources (static context) -----

  server.resource(
    "architecture-index",
    "dreammeta://architecture-index",
    {
      description:
        "Meta-Department architecture index (元部门架构索引) — the core governance document defining the 13-atom system, three-layer gravity structure, and runtime binding rules.",
      mimeType: "text/markdown",
    },
    async (uri) => ({
      contents: [
        {
          uri: uri.href,
          mimeType: "text/markdown",
          text:
            architectureIndex ??
            "# architecture-index\n\nFile not found: .claude/agents/CLAUDE.md",
        },
      ],
    })
  );

  server.resource(
    "meta-command",
    "dreammeta://meta-command",
    {
      description:
        "Meta-Department /meta command definition (元部门 /meta 命令) — the workflow definition for invoking the Meta-Department orchestration chain.",
      mimeType: "text/markdown",
    },
    async (uri) => ({
      contents: [
        {
          uri: uri.href,
          mimeType: "text/markdown",
          text:
            metaCommand ??
            "# meta-command\n\nFile not found: .claude/commands/meta.md",
        },
      ],
    })
  );

  // ----- Tools (dynamic queries) -----

  server.tool(
    "list_atoms",
    "List all 13 atoms of the Meta-Department with their ID, name, layer, and core responsibility. Returns a structured overview of the three-layer gravity architecture (列出元部门 13 原子概要).",
    {},
    async () => {
      if (atoms.length === 0) {
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(
                {
                  error: "No atom files found",
                  searchPath: agentsDir,
                },
                null,
                2
              ),
            },
          ],
        };
      }

      const summary = atoms.map((a) => ({
        id: a.id,
        name: a.name,
        layer: a.layer,
        layerLabel: a.layerLabel,
        coreResponsibility: a.coreResponsibility,
      }));

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(
              { count: summary.length, atoms: summary },
              null,
              2
            ),
          },
        ],
      };
    }
  );

  server.tool(
    "get_atom",
    "Get details of a single Meta-Department atom by its ID (e.g. M01, M09). Returns a summary by default, or the full atom definition when includeFullContent is true (获取单个原子定义).",
    {
      atomId: z
        .string()
        .regex(/^M\d{2}$/)
        .describe(
          "Atom identifier, e.g. M01, M09, M13"
        ),
      includeFullContent: z
        .boolean()
        .optional()
        .default(false)
        .describe(
          "If true, return the complete atom definition. Default false returns summary only."
        ),
    },
    async ({ atomId, includeFullContent }) => {
      const atom = atomMap.get(atomId);

      if (!atom) {
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(
                {
                  error: `Atom ${atomId} not found`,
                  available: atoms.map((a) => a.id),
                },
                null,
                2
              ),
            },
          ],
        };
      }

      const result = {
        id: atom.id,
        name: atom.name,
        layer: atom.layer,
        layerLabel: atom.layerLabel,
        coreResponsibility: atom.coreResponsibility,
      };

      if (includeFullContent) {
        result.fullContent = atom.fullContent;
      }

      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(result, null, 2),
          },
        ],
      };
    }
  );

  // ----- Connect via stdio -----

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((err) => {
  console.error("dreammeta-runtime fatal:", err);
  process.exit(1);
});
