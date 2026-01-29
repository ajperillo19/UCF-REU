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
totmag_pat      = re.compile(r"Total\s+Magnetization.*:\s*([-\d\.]+)", re.IGNORECASE)
absmag_pat      = re.compile(r"Absolute\s+Magnetization.*:\s*([-\d\.]+)", re.IGNORECASE)

# 3) Storage
data = {}   # site -> (energy, totmag, absmag)

for fn in files:
    m = fname_pat.search(fn)
    if not m:
        continue
    site = m.group(1)
    text = open(fn).read()
    me = energy_pat.search(text)
    mt = totmag_pat.search(text)
    ma = absmag_pat.search(text)
    if not (me and mt and ma):
        print(f"⚠️  skipping {site!r}:",
              "energy:", bool(me),
              "totmag:", bool(mt),
              "absmag:", bool(ma))
        continue
    data[site] = (
        float(me.group(1)),
        float(mt.group(1)),
        float(ma.group(1)),
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
totmag     = [data[s][1] if s in data else np.nan for s in sites]
absmag     = [data[s][2] if s in data else np.nan for s in sites]

marker_map = {'fcc':'o','hcp':'o','ontop':'o'}

# 6a) Plot energies
plt.figure(figsize=(6,4))
for xi, s in zip(x, sites):
    plt.scatter(xi, energies[sites.index(s)],
                marker=marker_map[s], s=100, label=s)
# Only one legend entry per site
handles, labels_ = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels_, handles))


plt.xticks(x, sites)
plt.xlim(-.1, len(sites)-.9)

plt.xlabel("Adsorption site")
plt.ylabel("Total Energy (Ry)")
plt.title("Co Adsorption Energies on MoS₂")

plt.tight_layout()
plt.savefig("Adsorp_en.png")
plt.show()

# 6b) Plot total magnetization
plt.figure(figsize=(6,4))
for xi, s in zip(x, sites):
    plt.scatter(xi, totmag[sites.index(s)],
                marker=marker_map[s], s=100, label=s)
handles, labels_ = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels_, handles))


plt.xticks(x, sites)
plt.xlim(-.1, len(sites)-.9)
plt.xlabel("Adsorption site")
plt.ylabel("Total Magnetization (μB/cell)")
plt.title("Total Magnetization vs Adsorption Site")
plt.tight_layout()
plt.savefig("Tot_mag_hcp.png")
plt.show()




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







