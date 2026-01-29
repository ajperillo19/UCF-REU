from ase import Atoms
from ase.build import bulk
from ase.visualize import view

a = 5.67
bulkGe = bulk('Ge', 'diamond', a= a)
view(bulkGe)

