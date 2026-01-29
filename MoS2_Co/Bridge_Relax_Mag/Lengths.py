from ase import Atoms
from ase.io import read
import numpy as np
import csv

bridge = read('rel_bridge.out', format = "espresso-out")

# Get top sulfur position
S_top = bridge.get_positions()[1]

# Get cobalt position
Co = bridge.get_positions()[3]

# Bond Length
bond = np.linalg.norm(S_top-Co)

# Height of Cobalt
height = Co[2]-S_top[2]


header = ['Bond Length (Å)', 'Height (Å)']

with open('Lengths.txt', 'w', newline='') as fout:
    writer = csv.writer(fout, delimiter='\t')
    writer.writerow(header)
    row = [f'{bond:.6f}', f'{height:.6f}']
    writer.writerow(row) 
