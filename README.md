# :one: Welcome!
---

**`UCF-REU`**  is a collection of python and shell scripts that I used during my REU at the University of Central Florida, where I worked under Talat Rahman
and her computational condensed matter group to perform density functional theory (DFT) calculations of cobalt-molybdenum disulfide monolayer structures.

I am new to Git, and I am adding these README files in retrospect; thus, if my documentation conventions are somewhat strange, I apologize. However, I will
do my best to ensure my procedure is clear so that it may be used as a reproducible workflow.

Before we begin, I strongly suggest referring to **`https://github.com/comet-group/dlePy/tree/master/TUTORIALS`** for the basics on getting started. Dr. Le's
tutorials were instrumental in helping me become accustomed to navigating the Atomic Simulation Environment (ASE) and Quantum Espresso (QE).

# :two: Workflow
---

The Quantum Espresso (QE) workflow can be decomposed into two primary objectives:
1. Optimizing atomic structures
2. DFT calculations (band structure, density of states, etc.)

Therefore, throughout this repository you will see that I have procedural scripts to optimize atomic structrues, and scripts that actually perform
electronic structure calculations and the like. The python scripts largely are used for scanning through QE output files to extract relevant data
for plotting and/or tabulation. With that said, let us begin with a schematic for the workflow. First, atomic structures will need to be built 
with ASE, a very friendly python library that can be used to build and visualize atomic structures. Documentation can be found here:
**`https://ase-lib.org/`**. One can then feed the geometries (atomic structures) created in ASE to QE, where energy calculations, etc. can be 
performed. Once your structures are built, you will need to optimize them in QE. This effectively creates the most stable atomic configuration
according to DFT. With this optimized structure, all relevant electronic structure calculations can then be performed.
