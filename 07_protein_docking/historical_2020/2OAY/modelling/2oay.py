from modeller import *
from modeller.automodel import *

log.verbose()
env = environ(rand_seed=-42)
env.io.atom_files_directory = './:../:../atom_files'
env.io.hetatm = True
env.io.water = True





a = automodel(env,
              alnfile='aligment.model',
              knowns=('2OAY'),
              sequence='model',
              assess_methods=(assess.GA341, assess.DOPE)) 

a.starting_model = 1
a.ending_model = 1

a.md_level = refine.very_slow

a.make()
