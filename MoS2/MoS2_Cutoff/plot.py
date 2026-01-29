import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

Data = np.loadtxt('data.dat')

cutoffs = Data[:,0]
energies = Data[:,1]



energies_eV = energies*13.60569312299
energies_keV = energies_eV/1000

# 4a) Plot Total Energy vs Cutoff: Save as png
plt.figure()
plt.plot(cutoffs, energies_eV, "o-", linewidth=1.5)

ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Kinetic‐energy Cutoff (Ry)")
plt.ylabel("Total Energy (eV)")
plt.title("Total Energy vs. KE Cutoff")
plt.grid(True)
plt.tight_layout()
plt.savefig("MoS2_Cut.png")

# Plot charge density
Data_rho = np.loadtxt('rho.txt')

charge = Data_rho[:,0]
energy = Data_rho[:,1]


energy_eV = energy*13.60569312299

plt.figure()
plt.plot(charge*70, energy_eV, "o-", linewidth=1.5)

ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.ScalarFormatter(useOffset=False, useMathText=False))
ax.ticklabel_format(style='plain', axis='y')

plt.xlabel("Charge Density Cutoff (Ry)")
plt.ylabel("Total Energy (eV)")
plt.title("Total Energy vs. Charge Density Cutoff")
plt.grid(True)
plt.tight_layout()
plt.savefig("MoS2_Charge.png")

