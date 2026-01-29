import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# Load Data
energy, dos_up, idos = np.loadtxt('dos.dat' , unpack=True)

efermi = -2.151
# Make Plot
plt.figure()
plt.plot(energy-efermi, dos_up, linewidth=2, color='red')
 

plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('Density of States (state/eV)')
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0,(8,10)))
plt.xlim(-5,5)
plt.ylim(0,5 )
#plt.fill_between(energy, 0, dos_up, where=(energy < efermi), facecolor = 'r', alpha = .25)

plt.title('Co Monolayer DOS With SOC')
plt.savefig('dos_Co_Mon_SOC.png')
plt.show()
