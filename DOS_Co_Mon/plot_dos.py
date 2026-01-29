import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# Load Data
energy, dos_up, dos_down, idos = np.loadtxt('dos.dat' , unpack=True)

efermi = -2.150
# Make Plot
plt.figure()
plt.plot(energy-efermi, dos_up, linewidth=2, color='red')
plt.plot(energy-efermi, dos_down*(-1), linewidth=2, color = 'blue')

plt.axhline(y=0, linewidth=0.5, color='k')
plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('Density of States (state/eV)')
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0,(8,10)))
plt.xlim(-5,5)
plt.ylim(-5,5 )
#plt.fill_between(energy, 0, dos_up, where=(energy < efermi), facecolor = 'r', alpha = .25)
#plt.fill_between(energy, 0, dos_down*(-1), where=(energy<efermi), facecolor = 'b', alpha = .25)
plt.title('Co Monolayer DOS')
plt.savefig('dos_Co_Mon.png')
plt.show()
