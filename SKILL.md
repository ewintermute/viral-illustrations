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
- **Font:** Barlow for labels and identifiers; Inter for numerical values
- **Size:** minimum `font-size="18"` — text must be legible in a video frame at reduced resolution. Prefer 20–24px for primary labels.
- **Maximum 2 text elements per illustration.** If you think you need 3, cut one.
- **No eyebrow text, subtitles, or clarifying secondary text.** One label per concept — not a label plus a descriptor underneath it. If the label needs explaining, it's the wrong label.
- **Colours:** normal labels = Periwinkle Mid `#8BA0D6`; emphasis/primary labels = Core White `#FBFFF6`. Do not use dimmed colors (`opacity < 1` on text), yellow, green, or red for text — these are hard to read against variable backgrounds in video.
- **Species names** must be in SVG italic: `font-style="italic"` (Barlow or Inter both support this)
- **No titles, headers, or story names** in the SVG
- Labels describe what something IS: `"O. unilateralis"` not `"zombie-ant fungus parasitizes carpenter ants"`
- Text must be in the `label` group

### Chemical Structure Drawing (RDKit)

For any molecule that needs to appear in an illustration, use RDKit to generate an accurate 2D structure SVG rather than drawing it by hand.

**Tool:** `scripts/chem/draw_molecule.py`

```bash
python3 scripts/chem/draw_molecule.py "<SMILES>" output.svg [options]

Options:
  --width INT              SVG width (default 400)
  --height INT             SVG height (default 300)
  --highlight-smarts STR   SMARTS pattern — matching atoms/bonds drawn in Core Red #CA1E08
  --light                  Light background (default is dark #1C1E35)
```

**Output:** AWW-styled SVG with periwinkle bonds (#D1DCFF), coral oxygen labels (#E85542), Core Red highlights, Core Midnight background.

**Embedding in illustration SVG:**
1. Generate the molecule SVG file
2. Encode it as a base64 data URI in Python: `base64.b64encode(open(file,'rb').read()).decode()`
3. Embed using `<image href="data:image/svg+xml;base64,..." x="..." y="..." width="..." height="..."/>` inside the appropriate layer group

**Key molecules and their SMILES:**
- Artemisinin: `C[C@@H]1CC[C@H]2C(=O)OC[C@@H]3[C@H]2O[O][C@@]13C` (highlight O-O with `--highlight-smarts "[O]-[O]"`)
- Cyclosporin A: complex — use PubChem CID 5284601 SMILES
- Rapamycin: complex — use PubChem CID 5284616 SMILES

**Finding SMILES:** Use PubChem (https://pubchem.ncbi.nlm.nih.gov) — search compound name, get Isomeric SMILES from the page.

**Never hand-draw chemical structures in SVG.** The geometry is too complex to get right manually and errors are obvious to scientists. Always use RDKit.

### Standard DNA Double Helix Construction

Reference file: `illustrations/dna-helix-spec.svg` — three canonical variants (standard, highlighted region, CRISPR cut).

**Biological parameters (B-DNA):**
- **10 base pairs per turn**
- **Strand B phase offset = 216°** — this creates the major groove (6 bp wide) and minor groove (4 bp wide). Do NOT use 180° (that produces a symmetric ladder, not a helix with grooves).
- Pitch `P` = choose based on illustration size. Default: `P = 100px` per turn → 10px per base pair.
- Half-width `hw` = choose based on illustration size. Default: `hw = 26px`.

**Construction algorithm (Python reference — must be followed exactly):**

```python
import math

def strand_path(cx, ya, yb, hw, P, helix_y0, phase_rad, step=3):
    """Polyline tracing a sinusoidal strand. t is ALWAYS relative to helix_y0."""
    pts = []
    y = ya
    while y <= yb + step:
        y_c = min(y, yb)
        t = 2 * math.pi * (y_c - helix_y0) / P + phase_rad  # helix_y0, not ya
        x = cx + hw * math.sin(t)
        pts.append(f"{x:.2f},{y_c:.1f}")
        y += step
    return "M " + " L ".join(pts)
```

**Key rules:**
1. **Strands are polylines** (step ≤ 4px), not bezier curves. This guarantees smooth sinusoids.
2. **Phase reference is always `helix_y0`** — the top of the helix, not the segment start. Using the segment start `ya` causes rung misalignment (this was v3's bug).
3. **Rungs connect exact strand x-positions**: at each base pair y, compute `xA = cx + hw*sin(t)` and `xB = cx + hw*sin(t + phase_b)` using the same `t = 2π*(y - helix_y0)/P`. The rung runs from `min(xA,xB)` to `max(xA,xB)`. Never fixed left/right edges.
4. **Rung opacity** = `max(0.13, cos(t))` when `cos(t) > 0`, else `0.13`. Rungs fade on the back face (inside the groove).
5. **Depth layering**: find strand crossings analytically at `t_cross = (π - phase_b)/2 + k*π`. Between crossings, the strand with higher x at the segment midpoint is drawn on top.
6. **Skip rungs** where both strands are within 1.5px of each other (at crossings) — they'd be invisible dots.

**Colours:**
- Strand A: Navy Vintage `#2D3E6B`
- Strand B: Slate Blue `#5B6FA8`
- Rungs: Periwinkle Mid `#8BA0D6` at variable opacity
- Highlighted region: Mustard `#E6B800` (front strand) + Goldenrod Dark `#B8860B` (back strand)
- Cut ends: Core Red `#CA1E08`, splay outward from helix axis

**Variants:**
- **Standard**: plain helix as above
- **Highlighted region**: apply `hi_col`/`hi_col2` to rungs and strands in the target range; add a dashed bracket rectangle around the region
- **CRISPR cut**: omit rungs and strands in the gap range; add splayed blunt-end paths in Core Red diverging outward at the cut, converging inward at the resumption; add `Δ32 bp` or appropriate label

### Standard Eye Construction
All critter eyes use the same three-layer anatomy regardless of organism:
1. **Sclera:** `<ellipse>` with rx:ry ratio ~1.25:1 (horizontal), `fill="#E8EEFF"`, `stroke="#D4A574" stroke-width="1.5"`
2. **Pupil:** `<circle>` at ~40-45% of sclera rx, `fill="#0D0D16"`
3. **Specular:** `<circle>` offset up-left, ~20-25% of sclera rx, `fill="#FBFFF6" opacity="0.85"`

Scale the whole assembly to the creature — small animals get rx=7-9, large animals rx=20+. Do not use plain `<circle>` for the sclera. Do not deviate from this structure for consistency across the illustration set.

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
