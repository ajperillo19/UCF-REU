from ase.build import mx2, add_adsorbate
from ase import Atoms
from ase.visualize import view
# 1) Build MoS2 single-layer structure
Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)

# 2) Get Unit Cell Coordinates
cell = Mo_S2.get_cell()
a1,a2,_ = cell

fcc_xy = (1/3)*a1 + (2/3)*a2

ads = add_adsorbate(Mo_S2, 'Co', height = 2.0, position = (float(fcc_xy[0]), float(fcc_xy[1])))

view(Mo_S2)
