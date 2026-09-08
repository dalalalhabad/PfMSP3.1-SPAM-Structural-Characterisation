# AlphaFold-model MD simulation — exploratory reassessment (2026)

This directory contains the setup and execution records for a 250-ns
molecular-dynamics simulation performed during the 2026 reassessment of
the historical PfMSP3.1 SPAM structural model.

## Important provenance note

The simulated structure was derived from the AlphaFold Database model
associated with accession:

`A0A8G1DNL0`

A0A8G1DNL0 contains 121 amino acids and does not sequence-match the
historical 139-aa PfMSP3.1 SPAM structural model used in the 2020
Master's project.

Therefore, this simulation should be interpreted specifically as
molecular-dynamics characterisation of the A0A8G1DNL0-derived model and
not as direct MD validation of the historical 139-aa SPAM structure.

The sequence-provenance investigation is documented in:

`../../../03_exploratory_AlphaFold_comparison/README.md`

This exploratory simulation is retained because it formed part of the
2026 investigation before the sequence mismatch was fully resolved.

## Directory contents

### Setup

`setup/`

Contains files retained from preparation of the MD system, including:

- `A0A8G1DNL0.fasta`
- `AF_model_clean.pdb`
- `em.mdp`
- `ions.mdp`
- `nvt.mdp`
- `npt.mdp`
- `index.ndx`
- `posre.itp`
- `topol.top`
- `md_250ns.tpr`

The retained topology records that the system was prepared with
GROMACS 2026.0 using the CHARMM36 July 2022 force field and the SPC
water option.

### Execution records

`logs/`

Contains:

- `md_250ns.log`
- `md_250ns.slurm`

The production simulation was executed on the La Trobe HPC using
GROMACS 2020.7.

The retained SLURM script documents continuation of the production
simulation using one node, 16 CPU threads and 64 GB memory, with
checkpoint continuation enabled.

## Energy minimisation

The retained energy-minimisation parameters include:

- steepest-descent minimisation;
- maximum 50,000 steps;
- energy tolerance of 1000 kJ mol^-1 nm^-1;
- PME electrostatics;
- 1.2-nm Coulomb cutoff; and
- 1.2-nm van der Waals cutoff.

## Equilibration

### NVT

The NVT equilibration used:

- 2-fs timestep;
- 50,000 steps;
- total duration of 100 ps;
- V-rescale temperature coupling;
- reference temperature of 300 K;
- LINCS bond constraints; and
- periodic boundary conditions in all dimensions.

### NPT

The NPT equilibration used:

- 2-fs timestep;
- 50,000 steps;
- total duration of 100 ps;
- V-rescale temperature coupling at 300 K;
- Parrinello-Rahman isotropic pressure coupling;
- reference pressure of 1 bar;
- pressure-coupling time constant of 2 ps; and
- compressibility of 4.5 × 10^-5 bar^-1.

## Production MD

The production-run parameters were verified directly from:

`md_250ns.tpr`

The production simulation used:

- MD integrator;
- timestep: 0.002 ps (2 fs);
- number of steps: 125,000,000;
- total intended simulation time: 250 ns;
- V-rescale temperature coupling;
- reference temperature: 300 K;
- temperature-coupling time constant: 0.1 ps;
- Parrinello-Rahman isotropic pressure coupling;
- reference pressure: 1 bar;
- pressure-coupling time constant: 2 ps;
- compressibility: 4.5 × 10^-5 bar^-1;
- PME electrostatics;
- Coulomb cutoff: 1.2 nm;
- van der Waals cutoff: 1.2 nm;
- LINCS constraint algorithm; and
- periodic boundary conditions in x, y and z.

Compressed trajectory output was configured every 5,000 steps, while
energy and log output were configured every 1,000 steps.

## Software provenance

System preparation and topology generation were performed using
GROMACS 2026.0 on macOS.

The production simulation was executed using GROMACS 2020.7 on the
La Trobe HPC system.

This distinction is retained for reproducibility and provenance.

## Analysis

Analysis outputs generated from this trajectory are stored under:

`../../../06_MD_analysis/further_investigation_2026/AlphaFold_model/`

These include:

- RMSD;
- RMSF;
- radius of gyration;
- hydrogen-bond analysis;
- solvent-accessible surface area;
- principal component analysis;
- clustering;
- helix-distance analysis; and
- secondary-structure analysis.

## Subsequent sequence-matched reassessment

Following identification of the sequence mismatch between A0A8G1DNL0
and the historical 139-aa SPAM construct, a separate sequence-matched
structural reassessment was undertaken.

Five AlphaFold 3 models generated from the exact historical 139-aa
sequence were evaluated directly against the experimental NMR
restraints associated with the SPAM-H1 region.

That analysis is documented separately under:

`../../../04_AF3_vs_experimental_NMR/`

The sequence-matched AF3/NMR reassessment supersedes this exploratory
A0A8G1DNL0 branch for direct comparison with the historical structural
model.

## Interpretation

This simulation represents genuine computational work performed during
the 2026 reassessment.

However, because the simulated A0A8G1DNL0-derived structure does not
sequence-match the historical 139-aa SPAM model, the simulation and its
downstream analyses should not be presented as direct validation of the
historical SPAM structure.

The work is retained for transparency and analytical provenance, while
the sequence-matched AF3/NMR analysis in
`04_AF3_vs_experimental_NMR/` provides the appropriate modern
reassessment of the historical 139-aa construct.