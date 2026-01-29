from ase.build import bulk, surface, hcp0001
from ase.visualize import view

a = 2.31

latt = 2.45
c = latt*1.62753
Cobulk = bulk( 'Co', 'hcp', a = latt, c = c)
bi_Co = hcp0001('Co', size = (1,1,2),  a=latt, c=c, vacuum = 7.5,orthogonal = False, periodic = False)


view(bi_Co)
