import seekpath
import numpy as np
import ase
from ase.io import read
from ase import Atoms
import spglib

# 1) Read the fixed input file so that there are no complications with converting 'magn=' to a float

atoms = read("relax_MoS2_Co_fix.out")

# 1a) Get cell coordinates
cell = atoms.get_cell()

# 1b) Get atomic positions
pos = atoms.get_positions()

# Convert fractional positions to Cartesian:
pos = (np.dot(pos, cell)).tolist()
numbers = [42, 16, 16, 27] #Atomic numbers corresponding the positions of the atoms

structure = (cell, pos, numbers)

# 2) Get K-point path
path_data = seekpath.get_path(structure, with_time_reversal = True)

# 3) Extract point coordinates
point_coords = path_data['point_coords']

for label, coord in point_coords.items():
    print(f"{label}: {coord}")
