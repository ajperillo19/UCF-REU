import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import math


def next_odd(x):
    n = math.ceil(x)

    return n if n%2 else n+1

# 1) Gather filenames
files = sorted(glob.glob("scf_kp_*.txt"))

num_k = []
num_grid = []
energies = []
#runtimes = []

# 2) Parse each file
for fname in files:

    with open(fname) as f:
        text = f.read()
    # extract Total Energy
    e = float(re.search(r"Total Energy.*:\s*([-\d\.]+)", text).group(1))
    # extract Run Time
#    rt = float(re.search(r"Run Time.*:\s*([\d\.]+)", text).group(1))
    # extract number of k points
    k = float(re.search(r"Number of k-ponts.*:\s*([\d\.]+)", text).group(1))
    # extract number of grid points
    ng = float(re.search(r"Number of grid points.*:\s*([\d\.]+)", text).group(1))

    # append elements to appropriate arrays
    num_grid.append(ng)
    num_k.append(k)
    energies.append(e)
 #   runtimes.append(rt)

# 3) Sort by number of grid points
idx = np.argsort(num_grid)
energies = np.array(energies)[idx]
#runtimes = np.array(runtimes)[idx]

# 3b) Convert 'energies' to ev to determine minimum threshold
# Minimum cutoff calculations will be done in 'min_KE_cut.py'


energies_eV = energies*13.60569312299
#energies_keV = energies_eV/1000

energies_arr = np.array(energies_eV)

#WE WILL NEED THIS STEP TO DETERMINE THE OPTIMIZED LATTICE PARAMETER USING THE EQUATION OF STATES IN A SEPARATE FILE. THIS CAN BE DONE IN ANOTHER SCRIPT BUT FOR CONVENIENCE, I WILL DO IT HERE. ALL I AM DOING IS PRINTING THE LATTICE PARAMETERS AND CORRESPONDING ENERGY ARRAYS TO A 2 COLUMN TABULATED DATA FILE

#with open('./Data_k.txt', 'w') as file:
    # open the output file once, wr
with open("k-grid.txt", "w") as grid_file:
    grid_file.write("kx   ky   kz   Energy (eV)\n")
    
    for k in range(3, 11):
        
        # compute z‐mesh
        z_k = 3*k/3.88*2.39
        z   = next_odd(z_k)
        mesh = [3*k, 3*k, z]
        
        # write this line to k‑grid.txt
        grid_file.write(f"{mesh[0]}   {mesh[1]}   {mesh[2]}     {energies_eV[k]}\n")      



    #for i in range(len(num_grid)):
     #   file.write(f'{num_grid[i]}\t{energies_eV[i]}\n')

# 4a) Plot Total Energy vs Number of grid points: Save as png
plt.figure()
plt.plot(num_grid, energies, "o-", linewidth=1.5)

ax = plt.gca()

ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Number of Grid Points")
plt.ylabel("Total Energy (Ry)")
plt.title("Total Energy vs. # of Grid Points")
plt.grid(True)
plt.tight_layout()
plt.savefig("energy_vs_gp.png")

# 4b) Plot Total Energy vs Numver of k points: Save as png
plt.figure()
plt.plot(num_k, energies_eV, "s--", linewidth=1.5)

ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Number of k-points in calculations")
plt.ylabel("Total Energy (eV)")
plt.title("Total Energy vs. # of k-points")
plt.grid(True)
plt.tight_layout()
plt.savefig("TotalE_vs_kp.png")




#5) Show figures
plt.show()

