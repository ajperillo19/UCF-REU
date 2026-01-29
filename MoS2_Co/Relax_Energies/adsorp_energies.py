#!/usr/bin/env python3
import re
import glob
import matplotlib.pyplot as plt

# 1) Gather all relevant output files
files = glob.glob("relax_MoS2_Co_*.txt")

labels = []
energies = []

# Regex patterns
filename_pat = re.compile(r"relax_MoS2_Co_(\w+)\.txt")
energy_pat   = re.compile(r"Total Energy.*:\s*([-\d\.]+)")

# 2) Extract label and energy for each file
for fname in sorted(files):
    # a) extract site label
    m = filename_pat.search(fname)
    if not m:
        continue
    label = m.group(1)
    
    # b) read content and parse energy
    text = open(fname).read()
    me = energy_pat.search(text)
    if me:
        labels.append(label)
        energies.append(float(me.group(1))*13.605)

# 3) Define a unique marker for each site
marker_map = {
    'fcc':   'o',
    'hcp':   '^',
    'ontop': 's',
    'bridge':'D'
}

# 4) Plot
plt.figure(figsize=(6,4))
for label, energy in zip(labels, energies):
    plt.scatter(label, energy,
                marker=marker_map.get(label, 'x'),
                s=100,
                label=label)

# Create a single legend entry per label -- develop a legend based on the axes object that contains the markers corresponding the the different adsorption sites
handles, leg_labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(leg_labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.xlabel("Adsorption site")
plt.ylabel("Total Energy (eV)")
plt.title("Co adsorption energies on MoS₂ monolayer")
plt.tight_layout()
plt.savefig("Co_MoS2_adsorption_energies.png")
plt.show()

