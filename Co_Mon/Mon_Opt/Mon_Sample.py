from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
from ase.visualize import view

#create Cobalt monolayer
a = 2.3055
c = a*1.62753
Cobulk = bulk( 'Co', 'hcp', a=a, c = c)
mono = hcp0001('Co', size = (1,1,1), a=a, c=c, vacuum = 7.5,orthogonal = False, periodic = False)


