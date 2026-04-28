import { describe, test } from "node:test";
import assert from "node:assert/strict";
import { promisify } from "node:util";
import { execFile } from "node:child_process";
import path from "node:path";
import { REPO_ROOT } from "./_helpers.mjs";

const execFileAsync = promisify(execFile);

describe("validate-run-artifact.mjs", () => {
  const validFixture = path.join(REPO_ROOT, "tests", "fixtures", "run-artifacts", "valid-run.json");
  const invalidFixture = path.join(REPO_ROOT, "tests", "fixtures", "run-artifacts", "invalid-run-public-ready.json");

  test("accepts a valid run artifact with full finding lineage", async () => {
    const { stdout } = await execFileAsync(
      "node",
      ["scripts/validate-run-artifact.mjs", validFixture],
      { cwd: REPO_ROOT }
    );
    const result = JSON.parse(stdout);
    assert.equal(result.ok, true);
    assert.ok(result.validatedPackets.includes("cardPlanPacket"));
    assert.ok(result.validatedPackets.includes("summaryPacket"));
  });

  test("rejects an invalid public-ready run artifact", async () => {
    await assert.rejects(
      execFileAsync("node", ["scripts/validate-run-artifact.mjs", invalidFixture], {
        cwd: REPO_ROOT,
      })
    );
  });
});
