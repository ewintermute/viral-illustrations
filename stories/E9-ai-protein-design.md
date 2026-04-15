# E9: Writing Proteins from Scratch

*Category: Biotechnology & Medicine*

## The Story

Proteins are the molecular machines of life. Every enzyme, every structural fiber, every receptor, every signaling molecule is a protein. Proteins are strings of amino acids—20 different types—that fold into precise three-dimensional shapes dictated by their sequences. For decades, the central challenge of structural biology was going in the other direction: given a protein, predict its shape. AlphaFold 2, released by DeepMind in 2021, largely solved that problem, predicting the structures of virtually every known protein with accuracy approaching experimental measurement.

The more ambitious challenge is the inverse: given a desired function, design a protein that performs it. Not by modifying an existing natural protein, but by creating a sequence—and a shape—that has never existed before in the history of life. De novo protein design.

Until recently, this was possible in principle but almost never successful in practice. The computational complexity of predicting how any given sequence would fold, let alone whether that fold would perform a desired function, was too great for available methods. Success rates were typically well below 10%: generate thousands of candidate sequences, synthesize and test them, and find that nearly all don't fold as predicted or have no useful activity.

RFdiffusion, developed by David Baker's laboratory at the University of Washington and published in 2023, changed the calculus. The model applies diffusion—the same class of generative AI models underlying image generators like Stable Diffusion—to protein structure. It trains on known protein structures, learning to reverse a process of adding noise to 3D coordinates. Given a user-specified constraint—"build a protein around this enzyme active site" or "design a binder for this receptor"—RFdiffusion generates a backbone structure from scratch. ProteinMPNN then optimizes the amino acid sequence that would fold into that structure. AlphaFold predicts whether the designed sequence would actually achieve the target shape. If it does, the protein is synthesized and tested.

The success rate jumped to over 80% for structure accuracy. The proteins produced by this pipeline fold correctly—unprecedented for de novo design. They bind their specified targets. Designed enzyme scaffolds show catalytic activity. In 2023, Baker's group published results showing that de novo designed proteins could function as protein logic gates in living T-cells, regulating gene expression in response to two simultaneous input signals—proteins that had never existed in any organism, performing a synthetic computational function inside a human cell.

RFdiffusion3, released in 2025, extended the model to handle essentially any molecule found inside cells—not just proteins, but small molecules, DNA, RNA, and metal cofactors—at atomic resolution. The updated model is ten times faster and can design proteins that interact with the molecular world inside a cell in essentially unlimited combinations.

The implications are staggering. The full space of possible proteins—estimated at 10^1,300 possible sequences for a 1,000-amino-acid protein—is vastly larger than the set of proteins that have evolved naturally. Evolution has explored a tiny fraction of this space, constrained by mutation rates, generation times, and the availability of genetic variation. Protein design with AI can, in principle, access regions of sequence and function space that natural evolution has never visited.

Practical applications in development or early deployment include: designed binders for cancer cell surface proteins to direct immune cells; enzymes that degrade plastic polymers with efficiency no natural enzyme achieves; vaccines presenting antigens in designed scaffolds that enhance immune responses; and therapeutic proteins targeting diseases for which no natural ligand exists. The first AI-designed enzyme to function inside a living cell—a milestone in synthetic biology—may already have been achieved by the time you read this.

## Key Facts

- AlphaFold 2 (2021) solved protein structure prediction; RFdiffusion (2023) reversed the problem—generating novel protein shapes from user-specified functional constraints
- RFdiffusion uses diffusion models (similar to AI image generators) trained on known protein structures to design protein backbones from scratch
- De novo design success rates jumped from <10% to >80% for structural accuracy using the RFdiffusion + ProteinMPNN + AlphaFold pipeline
- In 2023, de novo designed proteins were demonstrated to function as logic gates inside living human T-cells, regulating gene expression
- RFdiffusion3 (2025) handles all intracellular molecule types at atomic resolution, running 10× faster than the original

## References

- De novo design of protein structure and function with RFdiffusion — https://jclinic.mit.edu/research-project/de-novo-design-of-protein-structure-and-function-with-rfdiffusion/
- RFdiffusion: A generative model for protein design — https://www.bakerlab.org/2023/07/11/diffusion-model-for-protein-design/
- RFdiffusion3 now available — https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/
