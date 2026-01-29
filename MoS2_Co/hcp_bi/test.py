import numpy as np
from ase import Atoms
from ase.build import mx2, add_adsorbate

from ase.build import add_adsorbate
from ase.io import read, write

from ase.visualize import view

# 1) Read in your relaxed MoS2 slab
Mo_S2 = read('rel_opt.out')

# 2) Enlarge the c‐axis (vacuum)
Mo_S2.cell[2,2] = 25.0

# 3) Identify your hcp site in (x,y).  
#    Here you used (0,0) in Cartesian; if that's already your hcp hollow, great.
hcp_xy = (0.0, 0.0)

# 4) Add *two* Co adsorbate layers at different heights
heights = [2.0,   # first Co layer ~2 Å above top S
           2.0+2.03]  # second Co layer, ~2.03 Å above the first (Co–Co spacing in hcp)
for h in heights:
    add_adsorbate(Mo_S2, 'Co', height=h, position=hcp_xy)

# 5) Tile in x,y to get your full 2D supercell  
#    (e.g. a 4×4 MoS2 with two Co layers)
#o_S2 = Mo_S2.repeat((4, 4, 1))

# 6) Write it out or view
write('MoS2_2Co_layers.xyz', Mo_S2)
view(Mo_S2)


