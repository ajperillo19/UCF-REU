from ase.build import  bulk, surface, add_vacuum, hcp0001
from ase.visualize import view

latt = 2.45
c = latt*1.62753
Cobulk = bulk( 'Co', 'hcp', a = latt, c = c)



mono = hcp0001('Co', size = (1,1,1),  a=latt, c=c, vacuum = 7.5,orthogonal = False, periodic = False) 

view(mono)
