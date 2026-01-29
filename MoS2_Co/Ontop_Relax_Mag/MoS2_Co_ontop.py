from ase.build import mx2, add_adsorbate
from ase.visualize import view
from ase import Atoms

Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)

# 1) Get Sulfur Positions
pos = Mo_S2.positions

pos_S1_x = pos[1][0]
#print(pos_S1_x)

pos_S1_y = pos[1][1]
#print(pos_S1_y)

pos_S1_z = pos[1][2]
#print(pos_S1_z)

pos_S2_x = pos[2][0]
#print(pos_S2_x)
pos_S2_y = pos[2][1]
#print(pos_S2_y)
pos_S2_z = pos[2][2]
#print(pos_S2_z)

# 2) Add Cobalt Atom On-top of Sulfur

ads = add_adsorbate(Mo_S2, 'Co', height = 2.0, position = (pos_S2_x, pos_S2_y))


view(Mo_S2)
