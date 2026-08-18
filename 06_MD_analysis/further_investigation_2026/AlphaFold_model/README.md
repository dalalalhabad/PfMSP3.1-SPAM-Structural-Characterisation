# AlphaFold-model MD analysis — further investigation (2026)

This directory contains molecular-dynamics analyses performed in 2026 on the AlphaFoldDB-derived model associated with accession A0A8G1DNL0.

## Important provenance note

The A0A8G1DNL0 sequence contains 121 amino acids.

The historical PfMSP3.1 SPAM model used in the 2020 Master's project was based on a different 139-amino-acid sequence.

Direct comparison confirmed that A0A8G1DNL0 is not sequence-matched to the historical 139-aa SPAM modelling query.

Therefore, the analyses in this directory should be interpreted specifically as molecular-dynamics characterisation of the A0A8G1DNL0-derived model.

They should not be interpreted as direct validation of the historical 139-aa SPAM structural model.

Further details on the sequence comparison are documented in:

`../../../03_AlphaFold_validation/README.md`

## Analysis categories

### RMSD, RMSF and radius of gyration

Directory:

`RMSD_RMSF_Rg/`

Files include:

- `RMSD_250ns.xvg`
- `RMSF_CA_250ns.xvg`
- `Rg_250ns.xvg`

These contain structural-stability and compactness measurements calculated from the 250-ns MD trajectory.

### Hydrogen bonds and solvent-accessible surface area

Directory:

`HBond_SASA/`

Files include:

- `HBonds_250ns.xvg`
- `SASA_250ns.xvg`

These contain hydrogen-bond and solvent-accessible surface-area analyses from the 250-ns trajectory.

### Principal component analysis

Directory:

`PCA/`

Files include:

- `PC1_250ns.dat`
- `PC2_250ns.dat`
- `PCA_PC1_PC2_combined.dat`
- `average_250ns.pdb`
- `eigenval_250ns.xvg`
- `eigenvec_250ns.trr`

These files preserve the PCA and essential-dynamics analysis of the trajectory.

### Clustering

Directory:

`clustering/`

Files include cluster assignments, cluster sizes, transition information and representative structures.

The final clustering analysis used the `FINAL_080` output set.

The file:

`clusters_FINAL_080.xpm`

is a very large generated clustering matrix and is intentionally excluded from Git tracking through `.gitignore`.

Other clustering outputs remain preserved where their file sizes are suitable for the repository.

### Helix-distance analysis

Directory:

`helix_distances/`

Files include:

- `H1_H2_dist.xvg`
- `H1_H3_dist.xvg`
- `H2_H3_dist.xvg`
- cleaned distance data files where available

These analyses were used to examine distances between the helical regions during the trajectory.

### Secondary-structure analysis

Directory:

`secondary_structure/`

Files include:

- `SecondaryStructure_250ns.xpm`
- `SecondaryStructure_Count_250ns.xvg`

These files preserve the secondary-structure analysis over the 250-ns trajectory.

### Reproducibility records

Directory:

`reproducibility/`

This directory contains logs and intermediate clustering outputs associated with testing multiple clustering cut-offs and generating the final clustering analysis.

These files are retained to document how the final clustering result was obtained.

## Interpretation

These analyses represent genuine 2026 computational work and are retained as part of the project's investigation history.

However, because the analysed A0A8G1DNL0 model does not sequence-match the historical 139-aa SPAM model, results from this directory should not be used as direct evidence for the behaviour of the historical SPAM structure.

A sequence-matched modern structural prediction based on the exact historical 139-aa SPAM sequence would be required for a direct modern comparison.
