# Viral Illustrations — Project State
*Last updated: 2026-04-18*

---

## What This Is

A library of 120 biology story illustrations in the **American Wetware (AWW)** brand style — dark background, flat colours, scientific/editorial aesthetic. Each illustration is a 800×600 SVG scene paired with a written story (~500–700 words science journalism).

Stories live in `stories/`. Illustrations live in `illustrations/`.

Deployed at: **https://ewintermute.github.io/viral-illustrations/**

---

## Story Library

**120 stories** across 11 appeal categories:

| Category | Code | Count |
|---|---|---|
| Superlatives | A | 8 |
| Counterintuitive Twists | B | 12 |
| Danger/Death | C | 6 |
| Sex/Reproduction/Evolution | D | 7 |
| Money/Power/Economic Impact | E | 22 |
| Manipulation/Control | F | 12 |
| Origins/Identity | G | 5 |
| Microbiome | H | 8 |
| Extraordinary Senses | I | 12 |
| Human Genetics/Evolution | J | 13 |
| Biomaterials | K | 12 |

---

## Illustration Progress

**14 of 120 stories illustrated** (12% done):

| ID | Title |
|---|---|
| A6 | Mosquito — Deadliest Animal |
| A7 | Horseshoe Crab Blood |
| B8 | Contagious Cancer |
| B10 | Octopus RNA Editing ⭐ |
| C1 | Zombie Ant Fungus |
| D4 | Anglerfish Fusion |
| E16 | Artemisinin |
| F2 | Toxoplasma Mice |
| F6 | Sacculina Barnacle |
| H2 | Fecal Transplant |
| I2 | Bird Quantum Navigation |
| J13 | CRISPR Babies |
| K11 | Termite AC |
| K8 | Mantis Shrimp Club |

⭐ B10 uses Version C from the Gemini synthesis experiment (conceptual/mechanism split layout)

**106 stories still need illustrations.**

---

## Model Comparison Experiment

A benchmark comparing 10 AI models on the same 5 test illustrations (C1, A7, B10, D4, K8):

**Page:** https://ewintermute.github.io/viral-illustrations/model-comparison.html

| Model | Folder | Notes |
|---|---|---|
| Claude Opus 4.6 | `model-test/claude-opus/` | |
| GPT-4o | `model-test/gpt4o/` | |
| Gemini 2.5 Pro | `model-test/gemini-25-pro/` | |
| Gemini 3.1 Pro | `model-test/gemini-31-pro/` | |
| DeepSeek V3 | `model-test/deepseek-v3/` | |
| Qwen3 | `model-test/qwen3/` | Added 2026-04-17 |
| o4-mini | `model-test/o4-mini/` | Added 2026-04-17 |
| Gemini 2.0 Flash | `model-test/gemini-20-flash/` | Added 2026-04-17 |
| Claude Sonnet 4.5 | `model-test/claude-sonnet-45/` | Added 2026-04-17 |
| Llama 4 Maverick | `model-test/llama4-maverick/` | No tool support — generated via direct API call |

---

## Gemini Feedback Experiments

### Experiment 1 — Iterative Feedback (D4: Anglerfish Fusion)
**Page:** https://ewintermute.github.io/viral-illustrations/experiment-gemini-feedback/

Pipeline: Claude generates SVG → Gemini Vision critiques → Claude regenerates with feedback.

Result: Round 2 showed clear improvements — larger female body, more absorbed fused males, dramatically expanded lure glow (12 concentric rings), pure black background, better composition.

### Experiment 2 — Multi-Version Synthesis (B10: Octopus RNA Editing)
**Page:** https://ewintermute.github.io/viral-illustrations/experiment-gemini-synthesis/

Pipeline: Claude generates 3 visually distinct versions in parallel → Gemini Vision synthesises the best elements from all three → Claude executes the combined brief.

Versions:
- A: Close-up intimate (arm detail + A→I inset diagram)
- B: Wide environmental (full octopus, cold/warm temperature zones)
- C: Conceptual split (octopus + RNA mechanism diagram panel) ← **Jake's preferred version, now the canonical B10 illustration**

---

## Cost Estimate (remaining 106 illustrations)

Using Claude Opus 4.6 (~$0.40/illustration): **~$42–55**
Using Claude Sonnet 4.5 (~4× cheaper): **~$12–15**

Recommendation: run Sonnet for bulk, Opus for hero/featured illustrations.

---

## Style Reference

- **Skill file:** `skills/aww-illustration/SKILL.md`
- **Style guide:** `2026-04-15 viral-illustrations/aww-style-guide-v2.md`
- **Canvas:** 800×600, viewBox="0 0 800 600"
- **Background:** Flat `#1C1E35` or `#0D0D16`. No gradients, no filters.
- **Key colours:** Green `#2FBF39`, Yellow `#FFFF77`, Periwinkle `#D1DCFF`, Slate `#5B6FA8`

---

## Repo

`git@github.com:ewintermute/viral-illustrations.git`
