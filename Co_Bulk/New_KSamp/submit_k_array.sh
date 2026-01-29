#!/bin/bash
#SBATCH --job-name=ecut_scf
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --time=10:00:00
#SBATCH --error=%A_%a.err
#SBATCH --output=%A_%a.out
#SBATCH --array=0-12       # indices 0 through 12 (13 tasks total)

# 1) Define your list of cutoffs in the same order as --array indices:
k_Values=(1 2 3 4 5 6 7 8 9 10)

# 2) Pick the correct cutoff based on the array task ID
k=${k_Values[$SLURM_ARRAY_TASK_ID]}

# 3) Load modules and set up environment
module purge
module load qe/7.2
export OMP_NUM_THREADS=1

# 4) Build the input/output filenames
#    Note: zero-pad to two digits if needed (e.g. 05, 20, 80)
k_str=$(printf "%02d" $k)
input_file="scf_${k_str}.inp"
output_file="scf_${k_str}.out"

# 5) Run pw.x for this cutoff
mpirun pw.x < $input_file > $output_file

