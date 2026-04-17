#!/usr/bin/env python3
"""
AWW Chemical Structure SVG Generator
Usage: python3 draw_molecule.py <SMILES> <output.svg> [options]

Options:
  --width  INT     SVG width in px (default 400)
  --height INT     SVG height in px (default 300)
  --highlight-smarts SMARTS  SMARTS pattern for atoms/bonds to highlight in Core Red
  --dark           Dark background (Core Midnight #1C1E35) — default
  --light          Light background (Core White #FBFFF6)

The output SVG is styled for AWW brand:
  Bonds/atoms: Periwinkle Mid #D1DCFF
  Oxygen labels: Coral Red #E85542
  Highlighted atoms/bonds: Core Red #CA1E08
  Background: Core Midnight #1C1E35 (default)
"""
import sys, argparse, re
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

def draw(smiles, outfile, width=400, height=300, highlight_smarts=None, dark=True):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        sys.exit(f"Invalid SMILES: {smiles}")
    # Remove stereo — flat planar skeletal structures only
    Chem.rdmolops.RemoveStereochemistry(mol)
    # CoordGen (Schrödinger algorithm) produces cleaner ring layouts than default
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)

    highlight_atoms, highlight_bonds, atom_colors, bond_colors = [], [], {}, {}
    if highlight_smarts:
        query = Chem.MolFromSmarts(highlight_smarts)
        matches = mol.GetSubstructMatches(query)
        for match in matches:
            for idx in match:
                highlight_atoms.append(idx)
                atom_colors[idx] = (0.79, 0.12, 0.03, 1.0)  # Core Red
        # highlight bonds between matched atoms
        matched_set = set(highlight_atoms)
        for bond in mol.GetBonds():
            if bond.GetBeginAtomIdx() in matched_set and bond.GetEndAtomIdx() in matched_set:
                highlight_bonds.append(bond.GetIdx())
                bond_colors[bond.GetIdx()] = (0.79, 0.12, 0.03, 1.0)

    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    opts = drawer.drawOptions()
    if dark:
        opts.backgroundColour = (0.110, 0.118, 0.208, 1.0)  # #1C1E35
    else:
        opts.backgroundColour = (0.984, 1.0, 0.965, 1.0)    # #FBFFF6
    opts.bondLineWidth = 2.5
    opts.addStereoAnnotation = False
    opts.padding = 0.12

    drawer.DrawMolecule(mol,
        highlightAtoms=highlight_atoms if highlight_atoms else None,
        highlightBonds=highlight_bonds if highlight_bonds else None,
        highlightAtomColors=atom_colors if atom_colors else None,
        highlightBondColors=bond_colors if bond_colors else None)
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()

    # Re-style for AWW
    if dark:
        svg = svg.replace("stroke:#000000", "stroke:#D1DCFF")
        svg = svg.replace("fill:#000000",   "fill:#D1DCFF")
        svg = svg.replace("fill:#FF0000",   "fill:#E85542")   # O labels
        svg = re.sub(r"fill:#FFFFFF", "fill:#1C1E35", svg)
    else:
        svg = svg.replace("fill:#FFFFFF", "fill:#FBFFF6")

    with open(outfile, 'w') as f:
        f.write(svg)
    print(f"Written: {outfile} ({len(svg)} bytes)")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('smiles')
    p.add_argument('outfile')
    p.add_argument('--width',  type=int, default=400)
    p.add_argument('--height', type=int, default=300)
    p.add_argument('--highlight-smarts', default=None)
    p.add_argument('--light', action='store_true')
    args = p.parse_args()
    draw(args.smiles, args.outfile,
         args.width, args.height,
         args.highlight_smarts,
         dark=not args.light)
