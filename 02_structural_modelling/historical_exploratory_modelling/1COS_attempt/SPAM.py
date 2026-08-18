from modeller import *
from modeller.automodel import *

log.verbose()
env = environ(rand_seed=-42)
env.io.atom_files_directory = './:../:../atom_files'
env.io.hetatm = True
env.io.water = True

class MyModel(automodel):
    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
        rsr.add(secondary_structure.alpha(self.residue_range('12:', '39:')))
        rsr.add(secondary_structure.alpha(self.residue_range('56:', '83:')))
        rsr.add(secondary_structure.alpha(self.residue_range('107:', '134:')))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['NZ:13'],
                                                         at['CD:78']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:20'],
                                                         at['NZ:74']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:27'],
                                                         at['NZ:64']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CG:76'],
                                                         at['NZ:129']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CA:55'],
                                                         at['NZ:108']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:39'],
                                                         at['NZ:106']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:32'],
:q:q                                                         at['NZ:113']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CG:25'],
                                                         at['NZ:120']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CG:18'],
                                                         at['NZ:127']),
                               mean=5, stdev=0.1))

a = MyModel(env,
vi              alnfile='aligment.model',
              knowns=('1psm'),
              sequence='model')


a.starting_model = 1
a.ending_model = 1

a.md_level = refine.very_slow

a.make()

