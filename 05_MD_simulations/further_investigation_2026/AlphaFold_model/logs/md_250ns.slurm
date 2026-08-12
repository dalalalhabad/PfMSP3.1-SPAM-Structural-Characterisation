#!/bin/bash
#SBATCH --job-name=SPAM250
#SBATCH --partition=month
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=30-00:00
#SBATCH --mem=64G
#SBATCH --output=md_%j.out
#SBATCH --error=md_%j.err

cd $SLURM_SUBMIT_DIR

/home/ad/18201791/software/gromacs-2020.7/bin/gmx mdrun \
-deffnm md_250ns_part6 \
-s md_250ns.tpr \
-nt 16 \
-cpi md_250ns_part5.cpt \
-noappend
