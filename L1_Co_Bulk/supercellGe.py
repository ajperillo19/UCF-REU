from ase import Atoms
from ase.build import bulk
from ase.visualize import view

a = 5.67*1.05
bulkGe = bulk('Ge', 'diamond', a= a)

supercellGe = bulkGe*(3,3,3)
view(supercellGe)


