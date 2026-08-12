#!/bin/bash
#SBATCH --job-name=“SPAM_replicate_2”         # Job name

# The batch details for the job
#SBATCH -p gpgpu                              # Machine
#SBATCH -A pLaTr0001                          # Group
#SBATCH --ntasks=6                            # Run on six CPUs
#SBATCH --gres=gpu:1                          # Use GPU processors
#SBATCH --time=7-00:00:00                     # Time limit days-hrs:min:sec
#SBATCH --output="rep2.log"                   # Output and error log
#SBATCH --gres-flags=enforce-binding

module load gcc/8.3.0 cuda/10.1.243 openmpi/3.1.4
module load fosscuda/2019b
module load gcc/8.3.0 openmpi/3.1.4
module load gromacs/2020
export GMX_MAXBACKUP=-1
export OMP_NUM_THREADS=6
# run replicate 2

gmx mdrun -s rep2.tpr -cpi rep2.cpt -deffnm rep2 -nb gpu -noappend 



		
