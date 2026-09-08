# Final AF3–Experimental NMR Reassessment

## Status

Completed: August 2026

Outcome: The historical PfMSP3.1/SPAM structural-modelling branch will not be pursued further for publication on the basis of the present reassessment.

## Background

The historical PfMSP3.1 structural-characterisation work used computational modelling to investigate the SPAM-containing region of PfMSP3.1.

In 2026, a modern AlphaFold 3 (AF3) prediction package for the same 139-aa sequence was supplied by Prof. Brian Smith.

The purpose of the reassessment was to determine whether the AF3 prediction was compatible with the original experimental NMR evidence and, specifically, whether the historical computational model resolved experimental inconsistencies that were not explained by AF3.

The deposited 1PSM coordinate ensemble was therefore not treated as the primary experimental benchmark. The principal comparison was made against the underlying experimental NMR restraints.

## AF3 input

The AF3 prediction used the same 139-aa sequence as the historical modelling work:

DDQKDIEAYKKAKQASQDAEQAAKDAENASKEAEEAAKEAVNLKESDKSYTKAKEACTAASKAKKAVETALKAKDDAETALKTSETPEKPSRINLFSRKTKEYAEKAKNAYEKAKNAYQKANQAVLKAKEASSYDYILG

Five AF3 coordinate predictions were supplied:

- sample 0
- sample 1
- sample 2
- sample 3
- sample 4

The original AF3 package and associated confidence information were retained unchanged.

## Experimental NMR data

The original experimental restraint file associated with 1PSM was retrieved and audited.

The restraint file contained 338 assign statements.

Particular attention was given to experimentally observed medium-range contacts, including i→i+4 restraints associated with alpha-helical structure.

Residue numbering between the experimental NMR construct and the 139-aa modelling construct was explicitly mapped before structural evaluation.

## Hydrogenation and atom mapping

The AF3 coordinate models did not contain all hydrogen atoms required for direct proton–proton distance evaluation.

Hydrogenated working copies were therefore generated using OpenMM while retaining the original AF3 files unchanged.

Atom-name mapping was audited to account for differences between legacy NMR naming conventions and modern coordinate-file atom nomenclature.

Ambiguous/pseudoatom restraints were evaluated using compatible proton groups rather than assuming a single stereospecific proton assignment.

## i→i+4 experimental restraints

Fourteen experimentally identified i→i+4 distance restraints were evaluated against all five AF3 models.

Results:

- AF3 sample 0: 14/14 satisfied
- AF3 sample 1: 14/14 satisfied
- AF3 sample 2: 14/14 satisfied
- AF3 sample 3: 14/14 satisfied
- AF3 sample 4: 14/14 satisfied

Thus, all five AF3 models satisfied 100% of the evaluated i→i+4 restraints.

These results strongly support compatibility of the AF3 prediction with the principal medium-range NMR observations associated with the experimentally identified helical structure.

## Full experimental distance-restraint audit

A broader audit was also performed against the available experimental distance restraints.

Restraints were stratified according to sequence separation and restraint type, including direct unambiguous, pseudoatom-group and legacy stereospecific assignments.

Several apparent distance violations were observed in individual static AF3 structures.

However, these should not automatically be interpreted as contradictions of the experimental NMR data.

NMR-derived distances reflect measurements arising from an ensemble of conformational states. A single static structure cannot necessarily reproduce every ensemble-averaged separation, particularly in flexible regions.

Therefore, individual apparent violations require cautious interpretation and do not by themselves demonstrate incompatibility between AF3 and the experimental NMR evidence.

## Consensus violation analysis

Potential violations recurring across multiple AF3 models were identified and examined separately.

This analysis was used to distinguish isolated model-specific deviations from recurrent geometric differences.

The consensus analysis did not provide evidence sufficient to establish that the AF3 prediction is fundamentally incompatible with the experimental NMR observations.

## Historical model comparison

The original historical MODELLER model was preserved unchanged and independently evaluated.

The historical model and AF3 predictions were also structurally aligned.

Although full-length comparison of the 139-aa structures produced large RMSD values, this was primarily associated with differences outside the experimentally constrained local region and should not be interpreted as evidence that the experimentally supported local structures are fundamentally different.

Within the experimentally relevant SPAM-H1 region, historical-model versus AF3 C-alpha RMSDs were approximately:

- sample 0: 0.840 Å
- sample 1: 0.887 Å
- sample 2: 0.846 Å
- sample 3: 0.842 Å
- sample 4: 0.774 Å

Within the principal experimental helical region, residues 16–41 of the 139-aa construct, C-alpha RMSDs were approximately:

- sample 0: 0.406 Å
- sample 1: 0.390 Å
- sample 2: 0.400 Å
- sample 3: 0.390 Å
- sample 4: 0.292 Å

These results demonstrate very close structural agreement between the historical model and AF3 within the experimentally relevant helical region.

The large full-length RMSD values therefore do not establish that the historical model provides a superior interpretation of the NMR evidence.

## Interpretation

The central question of this reassessment was not whether the historical model differed from AF3 or from the deposited 1PSM coordinates.

The relevant question was whether AF3 was inconsistent with the original experimental NMR evidence and whether the historical model resolved such inconsistencies.

The analyses performed here do not support that scenario.

Instead:

1. All five AF3 models satisfy all 14 evaluated i→i+4 experimental restraints.
2. AF3 and the historical model show very close agreement within the experimentally relevant helical region.
3. Apparent violations of some individual distance restraints in static structures must be interpreted in the context of NMR ensemble averaging and conformational flexibility.
4. No compelling experimental inconsistency was identified that is resolved uniquely by the historical model.

## Final scientific conclusion

The AF3 predictions are compatible with the available experimental NMR evidence for the PfMSP3.1/SPAM-H1 region.

The present reassessment does not demonstrate that the historical computational model provides a superior explanation of the experimental NMR observations.

Consequently, there is insufficient scientific justification, on the basis of these structural comparisons, to pursue publication of the historical model as a new structural result.

The historical modelling work remains a valid record of the computational analysis performed at the time. The 2026 AF3/NMR reassessment is retained separately as a transparent re-evaluation using modern structure prediction and direct comparison with the underlying experimental evidence.

## Decision following expert review

Following review of the reassessment, Prof. Brian Smith advised that NMR distance measurements should be interpreted in the context of structural ensembles and that individual static structures cannot be expected to reproduce all ensemble-derived distances, particularly in flexible regions.

Given the compatibility of AF3 with the available NMR evidence, he advised that the current results do not provide a basis for publication of the historical models.

Accordingly, no further analysis will be undertaken for the purpose of developing the historical structural model into a publication unless new experimental evidence or a substantially different scientific question emerges.

## Record retention

## Record retention

The following materials are retained either within this public repository or, where externally supplied or unsuitable for public Git distribution,
in the associated private project archive:

- original historical model;
- original AF3 prediction package;
- original experimental NMR restraint data;
- hydrogenated working structures;
- restraint-analysis scripts;
- AF3 distance-restraint results;
- i→i+4 restraint analysis;
- consensus violation analysis;
- historical-model restraint analysis;
- historical-model versus AF3 structural alignment;
- exploratory structure-prediction and sequence-mapping analyses.

No original source data or historical model files were modified as part of this reassessment.
