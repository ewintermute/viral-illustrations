# SKILL.md — AWW Viral Biology SVG Illustration Skill

**Version:** 1.0  
**Project:** viral-illustrations  
**Purpose:** Generate animation-ready SVG illustrations for biology story files in the American Wetware visual style.

---

## What This Skill Does

Given a biology story file from the `stories/` directory, this skill produces a single `.svg` file containing a flat, minimal scientific illustration. The SVG is structured for animation: every meaningful visual element is in a named group (`<g id="...">`) so individual parts can be targeted by a downstream animation step using CSS or GSAP.

---

## Animation Strategy: Layered Group Reveal

SVG files produced by this skill use a **layered group reveal** strategy. Each logical element of the illustration is isolated in its own `<g>` with a meaningful `id`. Animation layers proceed from background to foreground and from context to detail.

**Standard layer order:**
1. `bg` — background fill / scene environment
2. `context` — supporting elements (landscape, environment, scale reference)
3. `subject` — the primary biological subject (organism, molecule, process)
4. `detail-*` — specific structures being highlighted (one per named feature)
5. `label` — any minimal text callouts (used sparingly — see below)
6. `overlay` — arrows, emphasis marks, and annotation lines

This structure allows an animator to:
- Fade or draw in layers sequentially (`opacity: 0 → 1`)
- Use `stroke-dashoffset` reveal on paths in `detail-*` groups
- Translate or scale individual groups for entrance effects
- Stagger child elements within a group using GSAP's `stagger`

**Each `<g>` must have:**
- A meaningful `id` attribute (no auto-generated IDs)
- A `data-label` attribute describing what it represents in plain English
- Child elements that are logically grouped (don't mix unrelated shapes)

---

## Style Rules

### Canvas
- Viewbox: `0 0 800 600` (landscape) or `0 0 600 800` (portrait) — choose based on subject
- Background: Core Midnight (`#1C1E35`) for dramatic scientific subjects; Core White (`#FBFFF6`) for anatomical/botanical subjects
- No drop shadows except as explicit `<filter>` elements with IDs

### Color Usage (from aww-style-guide-v2.md)
- **Primary subject:** Core Green (`#2FBF39`) or Coral Red (`#E85542`) — choose one per illustration for the focal element
- **Secondary structures:** Periwinkle Mid (`#8BA0D6`), Mustard (`#E6B800`), Spring Light (`#6FD877`)
- **Backgrounds and environment:** Navy Vintage (`#2D3E6B`), Forest Deep (`#1A5C1E`), Fern Shade (`#248A28`)
- **Text and lines:** Core White (`#FBFFF6`) on dark backgrounds; Core Midnight (`#1C1E35`) on light backgrounds
- **Minimal use of Core Red (`#CA1E08`)** — reserve for one critical accent per illustration (e.g., danger signal, most important structure)
- **No gradients except** subtle radial glows for bioluminescent/fluorescent effects (max 2 stops, low opacity)

### Stroke Style
- Line weight: `stroke-width="1.5"` for fine detail, `stroke-width="2.5"` for primary outlines, `stroke-width="4"` for emphasis
- `stroke-linecap="round"` and `stroke-linejoin="round"` everywhere
- Dashed lines for non-physical relationships: `stroke-dasharray="6 4"`
- No hairlines (`stroke-width` below 1)

### Typography
- Font: Barlow for labels; Inter for data/values
- Font sizes: 14px minimum for any text (SVG `font-size`)
- Max 3 text elements per illustration
- Text must be part of the `label` group
- No titles, headers, or story names in the SVG
- Labels describe what something IS, not what it means (e.g., "spore" not "spores rain down onto ant trail")

### Shapes and Paths
- Prefer organic paths (`<path>`) over rigid rectangles for biological subjects
- Cell membranes, organism outlines, and leaves: use smooth bezier curves
- Geometric elements (crystals, lattices, engineered structures): use clean rectangles and polygons
- Avoid overly complex paths (keep node count reasonable for animation)

### No-go list
- No drop shadows via CSS
- No photographic textures or raster image embeds
- No clip-path complexity beyond simple rectangular masks
- No more than 2 gradient fills in a single SVG
- No titles or captions rendered as SVG text

---

## Process for Each Story

### Step 1: Identify the Visual Core
Read the story file. Answer: **What is the single most visually compelling moment or structure in this story?** This becomes the `subject` group. It should be identifiable in 1–2 seconds of looking at the illustration.

Examples:
- C1 (zombie ant fungus): the ant mid-bite with fungal stalk erupting
- A7 (horseshoe crab blood): the horseshoe crab with blue blood pooling out
- J13 (CRISPR babies): Cas9 scissors on a DNA strand

### Step 2: Choose a Composition
- **Close-up:** Focus on a molecule, cell, or small organism detail. Good for molecular mechanisms.
- **Scene:** Organism in environment with context elements. Good for behavioral/ecological stories.
- **Diagram:** Schematic of a process or system. Good for mechanisms with multiple steps.
- **Comparison:** Two or more subjects side by side with a clear visual contrast. Good for "X vs Y" stories.

### Step 3: Plan the Layer Stack
List all the `<g id="...">` groups before writing SVG. Each group should have a one-sentence description of what it shows and what animation action would reveal it (e.g., "fade in", "draw path", "scale from center").

### Step 4: Write the SVG
- Start with `<svg>` with `xmlns`, `viewBox`, `width`, `height` attributes
- Add a `<defs>` section for any reusable gradients or filters
- Write groups in layer order (bg first, overlay last)
- Use `<!-- comment -->` above each group to describe its content
- All paths must be closed or explicitly open (no ambiguous path endings)
- Test that all `id` attributes are unique within the file

### Step 5: Name the Output File
`[story-id]-illustration.svg` — e.g., `C1-zombie-ant-fungus-illustration.svg`

Save to `/illustrations/` directory within the project.

---

## Example Layer Plan (C1 — Zombie Ant Fungus)

```
bg           — dark forest floor, deep green/midnight
context      — leaf silhouettes, diffuse background ant colony trail
subject      — single ant, mandibles locked onto leaf vein, viewed from side
detail-hyphae — fungal network spreading through ant body (fine pale lines)
detail-stalk  — fruiting body erupting from head (Core Red stalk, spore cloud)
detail-spores — spore rain falling toward trail below (Core Yellow dots)
label        — minimal: "O. unilateralis" in Barlow, white, small
overlay      — height arrow (25cm indicator line, dashed)
```

---

## Example Layer Plan (A7 — Horseshoe Crab Blood)

```
bg           — dark ocean shelf, navy/midnight
context      — sandy bottom texture (subtle), horizon line
subject      — horseshoe crab viewed from above, carapace detail
detail-blood  — blue hemocyanin blood pooling from gill/sampling cut (Core Periwinkle)
detail-cell   — amebocyte cell enlarged inset (upper corner), showing clotting reaction
label        — "$60,000 / gallon" in Barlow Bold, Core Yellow
overlay      — inset border box, connection line from crab to cell detail
```

---

## Quality Checks

Before saving, verify:
- [ ] All `<g>` elements have `id` and `data-label` attributes
- [ ] No more than 3 text elements in the SVG
- [ ] Color values match the AWW palette (hex codes from style guide)
- [ ] No gradients except for bioluminescent/glow effects
- [ ] Layer order is bg → context → subject → detail → label → overlay
- [ ] File opens and renders correctly as SVG
- [ ] Filename matches story ID format

---

## Applying This Skill

When asked to generate an illustration for a story:

1. Read `stories/[story-id].md`
2. Read `aww-style-guide-v2.md` (color and font reference)
3. Follow Steps 1–5 above
4. Write the `.svg` to `illustrations/[story-id]-illustration.svg`
5. Output a brief note: visual core chosen, composition type, layer plan

For batches of multiple stories, process one at a time in full before moving to the next.
