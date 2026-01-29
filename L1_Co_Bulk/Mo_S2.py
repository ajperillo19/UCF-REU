
from ase.build import mx2
from ase.visualize import view
from ase import Atoms

Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.18, thickness = 3.19, size = (1,1,1), vacuum = None)

view(Mo_S2)
