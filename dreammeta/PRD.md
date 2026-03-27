# DreamMeta (梦元) Product Requirements Document

> Version: 1.0 | Date: 2026-03-20 | Status: Draft

---

## 1. Product Vision

DreamMeta is the **operations dashboard for Meta-Department (元部门) architecture** — a lightweight desktop tool that lets architects see, manage, and evolve their 13-atom agent systems across projects. It embodies "创造工具的工具": rather than doing agent work itself, it gives humans a clear window into structural health, configuration state, and cross-project reuse. The end state is a fast, local-first, minimalist control plane that makes the abstract architecture tangible and actionable.

## 2. Target Users

| User | Context | Primary Need |
|------|---------|-------------|
| **元部门架构师** | Designs/maintains 13-atom system across 1-5 projects | Structural visibility: health, completeness, drift |
| **Agent 开发者** | Edits M##-*.md files, adds skills/agents | Fast feedback loop: edit → see result instantly |
| **新项目接入者** | Bootstraps Meta-Department into existing projects | Quick start: init + track |

**Non-user**: End users of systems built with Meta-Department. DreamMeta is a builder's tool.

---

## 3. Current State Analysis (v0.3.0)

### 3.1 Architecture Assessment: B+

| Dimension | Rating | Notes |
|-----------|--------|-------|
| Code modularity | Good | Clean 4-layer: App → Screen → Data → Foundation |
| Theme system | A- | 27-field dataclass, 4 presets, JSON persistence |
| Data layer | B | Pydantic models, regex parser, no caching |
| Test coverage | C | 13 smoke tests only; no parser/renderer/interaction tests |

### 3.2 Technical Debt

| Item | Impact |
|------|--------|
| **~50% dead code**: collection.py, transform.py, absorb.py, adapters/, async_bridge.py, absorb_store.py, widgets/ | Confusion, maintenance burden |
| **Version mismatch**: pyproject.toml=0.2.0 vs app.py=0.3.0 | Trust issue |
| **Stale dreammeta/CLAUDE.md**: documents removed pages, old shortcuts | Onboarding friction |
| **No agent parse caching**: re-reads 13 files on every refresh | Wasteful (acceptable at current scale) |
| **Sync I/O on main thread**: project scanning blocks UI | Will degrade with >5 projects |

### 3.3 UX Pain Points (Priority Order)

| # | Pain Point | Severity |
|---|-----------|----------|
| P1 | No system-level health summary — user must mentally aggregate 13 buttons | High |
| P2 | Detail panel wastes 50% screen when nothing selected | High |
| P3 | Health indicators cryptic (bare Unicode, no tooltip/legend) | Medium |
| P4 | Read-only — can't even open file in external editor | Medium |
| P5 | No auto-refresh (manual click required after external edits) | Medium |
| P6 | Atom buttons cramped (3 lines + indicator in 56×100px) | Low |
| P7 | Layer labels low-contrast, undermining the most important visual hierarchy | Low |

---

## 4. User Stories & Requirements

### P0 — Must-Have (currently done)

| ID | Story | Status |
|----|-------|--------|
| US-01 | View 13-atom structural health at a glance | ✅ Done |
| US-02 | Read parsed agent detail with rendered markdown | ✅ Done |
| US-03 | Hot-reload agent definitions via Refresh | ✅ Done |
| US-04 | Initialize Meta-Department in a new project | ✅ Done |
| US-05 | View project health summary cards | ✅ Done |
| US-09 | Theme persistence across sessions | ✅ Done |

### P1 — Important for Daily Use (next iteration)

**US-06: Aggregate health summary**
> As an architect, I want to see "11/13 Healthy, 2 Warnings" at the top of the Atoms page so that I get instant system status.

Acceptance criteria:
- Summary bar above the layer graph showing healthy/warning/error counts
- Colored badges matching health states

**US-07: Open in external editor**
> As a developer, I want a button in the detail panel to open the current atom's .md file in my system default editor.

Acceptance criteria:
- "Open in Editor" button in detail panel header
- Uses `QDesktopServices.openUrl()` with file:// URL
- Works on Windows/macOS/Linux

**US-08: File watcher auto-refresh**
> As a developer, I want the Atoms page to auto-refresh when .md files change on disk so I don't need to manually click Refresh.

Acceptance criteria:
- `QFileSystemWatcher` on agents directory
- Debounced (500ms) to handle rapid successive writes
- Visual flash on changed atom button

**US-10: Health indicator tooltips**
> As an architect, I want to hover over an atom button and see which sections are missing so I can fix the issue.

Acceptance criteria:
- Tooltip shows "Missing: behavior_constraints, output_spec" or "All sections present"
- Health legend visible somewhere on the page

**US-11: Simplified atom button labels**
> As a user, I want less cramped atom buttons that show only M## and operation, with full name in tooltip.

Acceptance criteria:
- Button shows: `M04\n分` (ID + operation character only)
- Tooltip shows: "M04 分解元 (Decompose Meta)"
- Health indicator remains

### P2 — Power User Features (future)

| ID | Feature | Feasibility | Effort |
|----|---------|-------------|--------|
| US-12 | Inline atom editing (raw md + preview) | Medium | 2-3 days |
| US-13 | Cross-agent keyword search | Easy | 1-2 days |
| US-14 | Sidebar collapse animation (icon-only) | Easy | 1-2 days |
| US-15 | Dependency graph visualization | Hard | 4-5 days |
| US-16 | Command palette (Ctrl+K) | Medium | 2-3 days |
| US-17 | Cross-project atom diff view | Medium | 2-3 days |
| US-18 | Batch project health report export | Easy | 1 day |
| US-19 | Memory topic browser (read-only) | Medium | 2-3 days |
| US-20 | Drag-and-drop project import | Easy | 0.5-1 day |

---

## 5. Information Architecture (Target)

```
SIDEBAR (200px, collapsible to 48px)
  Brand: 梦元 DreamMeta
  ─────────────────────
  ◈ Atoms            ← 3-layer graph + detail (core page)
  ▣ Projects         ← project cards + init
  ─────────────────────
  ⚙ Settings         ← bottom, de-emphasized
```

### Atoms Page (Refined)

```
┌──────────────────────────────────────────────────┐
│  System Health: 11/13 ██████████░░ 85%           │
├──────────────┬───────────────────────────────────┤
│ Layer Graph   │  Detail Panel (collapsible)       │
│ (35% width)   │  ┌─ M04 分解元 ─────────────────┐│
│               │  │ Health: 5/5 ✔  [Open Editor] ││
│ [L3] ─────   │  ├─ 身份 ▼ ──────────────────────┤│
│ M09 M10...    │  │ (collapsed section)            ││
│ [L2] ─────   │  ├─ 核心职能 ▼ ──────────────────┤│
│ M04 M05...    │  │ (collapsed section)            ││
│ [L1] ─────   │  ├─ 行为约束 ▼ ──────────────────┤│
│ M01 M02 M03  │  │ (collapsed section)            ││
│               │  └──────────────────────────────┘│
└──────────────┴───────────────────────────────────┘
```

---

## 6. Technical Roadmap

### Phase 0: Clean Up (prerequisite)

- [ ] Delete dead code: collection.py, transform.py, absorb.py, adapters/, async_bridge.py, absorb_store.py, widgets/
- [ ] Sync version (use `importlib.metadata` as single source)
- [ ] Update dreammeta/CLAUDE.md to reflect 3-page architecture
- [ ] Extract markdown renderer to `utils/md_renderer.py`
- [ ] Remove unused models (AbsorbedItem) and constants (LAYER_COLORS)

### Phase 1: Core UX Fixes (P1 stories)

- [ ] US-06: Aggregate health summary bar
- [ ] US-10: Health indicator tooltips
- [ ] US-11: Simplified atom button labels
- [ ] US-07: "Open in Editor" button
- [ ] US-08: QFileSystemWatcher auto-refresh
- [ ] Strengthen layer label contrast

### Phase 2: Power Features (P2 selection)

- [ ] US-13: Cross-agent search
- [ ] US-14: Sidebar collapse
- [ ] US-12: Inline atom editing
- [ ] US-20: Drag-and-drop project import

### Phase 3: Visualization (P2)

- [ ] US-15: Dependency graph (static adjacency in constants.py + QPainter)
- [ ] US-16: Command palette

---

## 7. Non-Requirements (Scope Exclusions)

| Excluded | Rationale |
|----------|-----------|
| Agent runtime execution | DreamMeta manages tools, not executes them |
| Memory editing | Governed by M01; read-only browsing acceptable |
| Chat / LLM interaction | Not an LLM wrapper — it's a structural visibility tool |
| Cloud sync / accounts | Local-first, always |
| Multi-user collaboration | Collaboration via git |
| Plugin system | Premature |
| Domain-specific templates | Agent definitions are pure-abstract by design |
| Auto-update / telemetry | No phone-home behavior |

---

## 8. Design Principles

1. **Overview first, details on demand** — system health at a glance, drill down only when needed
2. **Minimalist** — every UI element must earn its pixel; remove before adding
3. **Local-first** — all data on filesystem, no network, no accounts
4. **Keyboard-friendly** — all primary actions accessible via shortcuts
5. **Configuration-as-architecture** — the .md files ARE the product; the app is the lens

---

## 9. Competitive References

| Tool | Key Insight for DreamMeta |
|------|--------------------------|
| **CrewAI Studio** | Three-panel layout (nav / canvas / detail); node-edge visualization |
| **IcePanel** | Hierarchical zoom (layer → atom → section); interactive drill-down |
| **Linear** | Monochrome-dominant, accent only for interactive elements; "warm grays" |
| **Obsidian** | Content-first; chrome is minimal; plugin-extensible |
| **Raycast** | Command palette as universal entry point; keyboard-first |
