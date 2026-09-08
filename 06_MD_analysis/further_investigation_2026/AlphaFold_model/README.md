# AlphaFold-model MD analysis — exploratory reassessment (2026)

This directory contains molecular-dynamics analyses performed in 2026 on
the AlphaFold Database-derived model associated with accession
A0A8G1DNL0.

## Important provenance note

The A0A8G1DNL0 sequence contains 121 amino acids.

The historical PfMSP3.1 SPAM model used in the 2020 Master's project was
based on a different 139-amino-acid sequence.

Direct comparison confirmed that A0A8G1DNL0 is not sequence-matched to
the historical 139-aa SPAM modelling query.

Accordingly, the analyses in this directory should be interpreted
specifically as molecular-dynamics characterisation of the
A0A8G1DNL0-derived model.

They should not be interpreted as direct validation of the historical
139-aa SPAM structural model.

The sequence-provenance investigation is documented in:

`../../../03_exploratory_AlphaFold_comparison/README.md`

This branch is retained as an exploratory part of the 2026 reassessment
for transparency and analytical provenance.

## Analysis categories

### RMSD, RMSF and radius of gyration

Directory:

`RMSD_RMSF_Rg/`

Files include:

- `RMSD_250ns.xvg`
- `RMSF_CA_250ns.xvg`
- `Rg_250ns.xvg`

These files contain structural-stability, flexibility and compactness
measurements calculated from the 250-ns MD trajectory.

### Hydrogen bonds and solvent-accessible surface area

Directory:

`HBond_SASA/`

Files include:

- `HBonds_250ns.xvg`
- `SASA_250ns.xvg`

These files contain hydrogen-bond and solvent-accessible surface-area
analyses generated from the 250-ns trajectory.

### Principal component analysis

Directory:

`PCA/`

Publicly retained outputs include:

- `PC1_250ns.dat`
- `PC2_250ns.dat`
- `PCA_PC1_PC2_combined.dat`
- `average_250ns.pdb`
- `eigenval_250ns.xvg`

These files preserve numerical and structural outputs from the PCA and
essential-dynamics analysis.

Large trajectory-derived or intermediate binary PCA files are not
required for interpretation of the public research record and may be
retained outside the Git repository.

### Clustering

Directory:

`clustering/`

The directory contains cluster assignments, cluster-size information,
transition outputs and representative structures.

The final clustering analysis used the `FINAL_080` output set.

The generated clustering matrix:

`clusters_FINAL_080.xpm`

is approximately 597 MB and is intentionally excluded from Git tracking
through `.gitignore`.

Smaller supporting clustering outputs are retained in the repository.

### Helix-distance analysis

Directory:

`helix_distances/`

Files include:

- `H1_H2_dist.xvg`
- `H1_H3_dist.xvg`
- `H2_H3_dist.xvg`
- cleaned distance data files where retained

These analyses were used to examine changes in distances between the
helical regions during the 250-ns trajectory.

### Secondary-structure analysis

Directory:

`secondary_structure/`

Files include:

- `SecondaryStructure_250ns.xpm`
- `SecondaryStructure_Count_250ns.xvg`

These files preserve the secondary-structure analysis performed across
the 250-ns trajectory.

### Reproducibility records

Directory:

`reproducibility/`

This directory contains logs and intermediate clustering outputs
associated with evaluating multiple clustering cut-offs and generating
the final clustering analysis.

These files are retained to document how the final clustering result was
selected.

## Relationship to the corresponding simulation

The simulation setup and execution records associated with these
analyses are stored under:

`../../../05_MD_simulations/further_investigation_2026/AlphaFold_model/`

The simulation and analysis directories should therefore be interpreted
together as one exploratory 2026 MD workflow.

## Subsequent sequence-matched reassessment

Following identification of the sequence mismatch between A0A8G1DNL0
and the historical 139-aa SPAM construct, the structural reassessment
proceeded using sequence-matched AlphaFold 3 predictions generated from
the exact historical 139-aa sequence.

Those AF3 models were evaluated directly against the experimental NMR
restraints associated with the SPAM-H1 region.

The sequence-matched reassessment is documented separately under:

`../../../04_AF3_vs_experimental_NMR/`

That analysis provides the appropriate modern structural reassessment of
the historical 139-aa construct.

The present A0A8G1DNL0-derived MD analyses are retained as exploratory
work and should not be used as direct evidence for the historical
139-aa model.

## Interpretation

These analyses represent genuine computational work performed during the
2026 reassessment.

Because the analysed A0A8G1DNL0-derived model does not sequence-match the
historical 139-aa SPAM model, the results should not be interpreted as
direct validation or rejection of the historical structural model.

Their value in this repository is as a transparent record of the
exploratory analysis that preceded the final sequence-matched AF3/NMR
reassessment.