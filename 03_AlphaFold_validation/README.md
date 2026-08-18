# AlphaFold validation investigation

This directory contains material examined during the 2026 further investigation of the historical PfMSP3.1 SPAM structural model.

## Important sequence-provenance finding

The AlphaFoldDB structure stored here corresponds to accession:

`A0A8G1DNL0`

The associated AlphaFold/UniProt sequence contains 121 amino acids.

By contrast, the historical SPAM structural model used in the 2020 Master's project was based on a 139-amino-acid sequence:

`sequence/SPAM_139aa_for_matched_AF_prediction.fasta`

Direct sequence comparison confirmed that these are not the same sequence.

- AlphaFoldDB A0A8G1DNL0 sequence length: 121 aa
- Historical SPAM modelling sequence length: 139 aa
- Exact sequence match: no

The AlphaFold PDB stored in:

`model/AF_model.pdb`

also contains 121 residues.

Therefore, A0A8G1DNL0 should not be interpreted as an AlphaFold prediction or direct structural validation of the historical 139-aa SPAM model.

## Files

### Sequence

`sequence/A0A8G1DNL0.fasta`

Sequence associated with the investigated AlphaFoldDB entry.

`sequence/A0A8G1DNL0.txt`

Historical UniProt/entry information associated with A0A8G1DNL0.

`sequence/SPAM_139aa_for_matched_AF_prediction.fasta`

Reconstructed 139-aa SPAM sequence corresponding to the historical structural-modelling query. This sequence should be used if a sequence-matched modern structure prediction is generated in future work.

### Model

`model/AF_model.pdb`

AlphaFoldDB structure associated with A0A8G1DNL0. This model contains 121 residues and does not correspond directly to the historical 139-aa SPAM sequence.

### Confidence

`confidence/AF-A0A8G1DNL0-F1-confidence_v6.json`

Per-residue AlphaFold confidence information associated with A0A8G1DNL0.

## 2026 molecular-dynamics analysis

A 250-ns molecular-dynamics investigation was performed on the A0A8G1DNL0-derived AlphaFold model during the 2026 further investigation.

The resulting analyses are preserved under:

`../06_MD_analysis/further_investigation_2026/AlphaFold_model/`

These results remain useful as a record of the 2026 investigation, but they should be interpreted specifically as analyses of the A0A8G1DNL0-derived model and not as validation of the historical 139-aa SPAM model.

## Future structural comparison

A direct AlphaFold comparison with the historical SPAM model should use a prediction generated from the exact 139-aa historical SPAM sequence.

No direct AlphaFold-versus-historical-model structural comparison is included at present. Such analysis should only be performed using a modern prediction generated from the exact historical 139-aa SPAM sequence.
