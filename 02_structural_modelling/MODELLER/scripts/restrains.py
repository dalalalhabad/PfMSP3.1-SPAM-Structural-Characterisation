Python 3.7.7 (v3.7.7:d7c567b08f, Mar 10 2020, 02:56:16) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>class MyModel(automodel):
    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
        rsr.add(secondary_structure.alpha(self.residue_range('6:', '42:')))
        rsr.add(secondary_structure.alpha(self.residue_range('49:', '80:')))
        rsr.add(secondary_structure.alpha(self.residue_range('97:', '129:')))
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
                               feature=features.distance(at['CD:55'],
                                                         at['NZ:108']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:39'],
                                                         at['NZ:106']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CD:32'],
                                                         at['NZ:113']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CG:25'],
                                                         at['NZ:120']),
                               mean=5, stdev=0.1))
        rsr.add(forms.gaussian(group=physical.xy_distance,
                               feature=features.distance(at['CG:18'],
                                                         at['NZ:127']),
                               mean=5, stdev=0.1))

