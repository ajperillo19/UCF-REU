import re
import glob
import matplotlib.pyplot as plt
import numpy as np
# 1) Gather all relevant output files
files = glob.glob("relax_MoS2_Co_*.txt")

labels = []
energies = []
total_mag = []
absolute_mag = []

# Regex patterns
filename_pat     = re.compile(r"relax_MoS2_Co_(\w+)\.txt")
energy_pat       = re.compile(r"Total Energy.*:\s*([-\d\.]+)")
total_mag_pat    = re.compile(r"Total Magnetization.*:\s*([-\d\.]+)")
absolute_mag_pat = re.compile(r"Absolute Magnetization.*:\s*([-\d\.]+)")

# 2) Extract label and energy for each file
for fname in sorted(files):
    # a) extract site label
    m = filename_pat.search(fname)
    if not m:
        continue
    label = m.group(1)
    
    # b) read content and parse energy/magnetization
    text = open(fname).read()
    me = energy_pat.search(text)
    tm = total_mag_pat.search(text)
    am = absolute_mag_pat.search(text)

    if me and tm and am:
        labels.append(label)
        energies.append(float(me.group(1)))
    
        total_mag.append(float(tm.group(1)))
        absolute_mag.append(float(am.group(1)))


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

# Create a single legend entry per label
handles, leg_labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(leg_labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.xlabel("Adsorption site")
plt.ylabel("Total Energy (eV)")
plt.title("Co adsorption energies on MoS₂ monolayer")
plt.tight_layout()
plt.savefig("Co_MoS2_adsorption_energies.png")
plt.show()


# 5) Plot Total Magnetization

#### Note: For some reason, the bridge site wasn't appearing in my plot when doing the magnetization calculations, it may be because of the way MatPlotlib displays initial data values; regardless, after several hours, I could not determine what the issue was, so I manually rewrote the plotting script

markers = ['o', '^', 's', 'D']

y = np.array(total_mag)
x = np.array([1,2,3,4])

my_xticks = ['bridge', 'hcp', 'fcc', 'ontop']


plt.figure(figsize=(6,4))
for label, tot_mag, marker in zip(x, y, markers):
    plt.scatter(label, tot_mag, marker=marker, s=100)
    
plt.xticks(x, my_xticks)

plt.xlabel("Adsorption site")
plt.ylabel("Total Magnetization (μB/cell)")
plt.title("Total Magnetization at Various Adsorption Sites")
plt.tight_layout()
plt.savefig("tot_mag_vs_adsorp.png")
plt.show()


# 6) Plot Absolute Magnetization
y_absolute = np.array(absolute_mag)
plt.figure(figsize=(6,4))
for label, ab_mag, marker in zip(x, y_absolute, markers):
    plt.scatter(label, ab_mag, marker = marker, s=100)


plt.xticks(x, my_xticks)
plt.xlabel("Absorption site")
plt.ylabel("Absolute Magnetization (μB/cell)")
plt.title("Absolute Magnetization at Adsorption Sites")
plt.tight_layout()
plt.savefig("abs_mag_vs_adsorp.png")
plt.show()



