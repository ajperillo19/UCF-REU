import re, glob
import numpy as np
import matplotlib.pyplot as plt
import csv
from ase.io import read

# 1) Find all your data files
files = sorted(glob.glob("rel_*.txt"))
print("Files:", files)

# 2) Prepare regexes 
fname_pat       = re.compile(r"rel_(\w+)\.txt")
energy_pat      = re.compile(r"Total\s+Energy.*:\s*([-\d\.]+)", re.IGNORECASE)

# 3) Storage
data = {}   # site -> (energy)

for fn in files:
    m = fname_pat.search(fn)
    if not m:
        continue
    site = m.group(1)
    text = open(fn).read()
    me = energy_pat.search(text)
    
    if not (me):
        print(f"⚠️  skipping {site!r}:",
              "energy:", bool(me))
        continue
    data[site] = (
        float(me.group(1)),
    )

print("Parsed data:", data)

# 4) Define the order of sites
sites = ['fcc','hcp','ontop']

# Warn if any missing
missing = [s for s in sites if s not in data]
if missing:
    print("Missing data for sites:", missing)

# 5) Build arrays for plotting
x = np.arange(len(sites))
energies   = [data[s][0] if s in data else np.nan for s in sites]


#7) Compute Energy Differences
sites = ['fcc','hcp','ontop']

# reference energy of MoS2 (eV)
MoS2 = read('/home/antonio/PROJ_MetalTMD/antonio/MoS2/Opt_Latt/Final_Structure/rel_opt.out',format="espresso-out")
E_ref = MoS2.get_total_energy()

# total energy of Cobalt bulk (eV)
Co = read('/home/antonio/PROJ_MetalTMD/antonio/Co_Bulk/Opt_Tot_En/scf.out', format = "espresso-out")
E_Co = Co.get_total_energy()/2


# total energy of bulk Co and MoS2 (eV)
E_tot = E_ref + E_Co


# 7b) Compute formation energy

# build header
# '\u0394' is the Unicode for delta
header = ['site', 'energy', '\u0394MoS2+Co', 'formation energy']

with open('form_en.txt', 'w', newline='') as fout:
    writer = csv.writer(fout, delimiter='\t')
    writer.writerow(header)

    for s in sites:
        E_s = data[s][0]*13.6057039763 # convert to eV from Ry
        # difference with total energy
        d_ref = E_tot - E_s
        
             
        pair_deltas = [E_s - data[other][0] for other in sites]
        row = [s, f"{E_s:.6f}", f"{d_ref:.6f}", f"{d_ref*-1:.6f}"] 
        writer.writerow(row)

print("Wrote form_en.txt")


# 8) Calculate adsoprtion Energy
path = '/home/antonio/PROJ_MetalTMD/antonio/Co_Mon/Mon_Opt/scf.out'

Co_atom = read(path, format = "espresso-out")

Co_energy = Co_atom.get_total_energy()

header_ads = header = ['site', 'energy (eV)','adsoprtion energy (eV)']
with open('ads_en.txt', 'w', newline='') as fout:
    writer = csv.writer(fout, delimiter='\t')
    writer.writerow(header)

    for s in sites:
        E_s = data[s][0]*13.6057039763 # convert to eV from Ry
        # difference with total energy
        d_ads = E_s - Co_energy - E_ref


        pair_deltas = [E_s - data[other][0] for other in sites]
        row = [s, f"{E_s:.6f}", f"{d_ads:.6f}"]
        writer.writerow(row)
print("Wrote ads_en.txt")





