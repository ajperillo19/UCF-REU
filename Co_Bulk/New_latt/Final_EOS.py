import numpy as np
from ase.eos import EquationOfState, birchmurnaghan
from ase.units import kJ
from matplotlib import pyplot as plt

# 1) load your data
data    = np.loadtxt('summary.csv', skiprows=1, delimiter=',', usecols=(1,2))
volumes = data[:,0]
energies = data[:,1]

# 2) shift energies so the lowest energy is zero
E0_min    = energies.min()
energies_rel = energies - E0_min

eos = EquationOfState(volumes, energies_rel)

# --- (you’ve already read volumes, energies_rel and done `eos = EquationOfState(...)`) ---

# 1) fit and get parameters
v0, e0_rel, B = eos.fit()        # same as before

# 2) build a smooth curve
V_fit = np.linspace(volumes.min(), volumes.max(), 200)

# ASE’s birchmurnaghan(V, E0, V0, B0, B1=4) returns the fitted energies:
E_fit = birchmurnaghan(V_fit, e0_rel, B0 = B,BP=4, V0 = v0)

# 3) plot manually
fig, ax = plt.subplots()
ax.scatter(volumes, energies_rel, color='C3', label='data')
ax.plot(V_fit,  E_fit,    'k--',  label='Birch–Murnaghan fit')

plt.axvline(x=23.414, ls = '--', c ='b', label = 'Optimized Volume: 23.414 Å³') 
ax.set_xlabel(r'$V$ (Å$^3$)')
ax.set_ylabel(r'$E - E_{\min}$ (eV)')
ax.legend()
plt.title('EOS Fitting')
plt.tight_layout()
plt.savefig('Final_EOS.png', dpi=300)
plt.show()

