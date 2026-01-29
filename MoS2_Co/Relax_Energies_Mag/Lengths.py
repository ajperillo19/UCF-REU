from ase import Atoms
from ase.io import read
import numpy as np
import csv
import os

paths = [
    '/home/antonio/PROJ_MetalTMD/antonio/MoS2_Co/fcc_relax_mag/rel_fcc.out',
    '/home/antonio/PROJ_MetalTMD/antonio/MoS2_Co/hcp_relax_mag/rel_hcp.out',
    '/home/antonio/PROJ_MetalTMD/antonio/MoS2_Co/Ontop_Relax_Mag/rel_on.out'
]

with open('Lengths.txt', 'w', newline='') as fout:
    writer = csv.writer(fout, delimiter='\t')
    writer.writerow(['site', 'Bond Length (Å)', 'Height (Å)'])

    for path in paths:
        # read the relaxed structure
        atoms = read(path, format='espresso-out')

        # Site label from filename
        site_label = os.path.basename(path).split('.')[0].replace('rel_', '')

        # Get top sulfur (index 1) and cobalt (index 3) positions
        pos = atoms.get_positions()
        S_top = pos[1]
        Co    = pos[3]

        # compute bond length and height
        bond   = np.linalg.norm(S_top - Co)
        height = Co[2] - S_top[2]

        # write the row
        writer.writerow([site_label, f"{bond:.6f}", f"{height:.6f}"])

print("Wrote Lengths.txt")

