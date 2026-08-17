#!/bin/bash
#SBATCH --job-name=“Complex499_replicate_3”         # Job name 

# The batch details for the job
#SBATCH -p gpgpu                              # Machine
#SBATCH -A pLaTr0001                          # Group
#SBATCH --ntasks=1                            # Run on six CPUs
#SBATCH --cpus-per-task=6
#SBATCH --gres=gpu:1                          # Use GPU processors
#SBATCH --time=5-00:00:00                     # Time limit days-hrs:min:sec
#SBATCH --output="rep3-499.log"               # Output and error log
#SBATCH --gres-flags=enforce-binding

module load gcc/8.3.0 cuda/10.1.243 openmpi/3.1.4
module load fosscuda/2019b
module load gcc/8.3.0 openmpi/3.1.4 
module load gromacs/2020
export GMX_MAXBACKUP=-1
export OMP_NUM_THREADS=6
# run replicate 3
 
gmx mdrun -v -deffnm 499 -cpi -s md_0_1.tpr -ntmpi 1 -ntomp 6


