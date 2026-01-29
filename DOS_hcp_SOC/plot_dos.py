import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# Load Data
energy, dos, idos = np.loadtxt('dos.dat' , unpack=True)

efermi = .007
# Make Plot
plt.figure()
plt.plot(energy-efermi, dos, linewidth=2, color='red')

plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('Density of States (state/eV)')

# Indicate Fermi Level and Band Gap
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0,(8,10)))

#plt.axvline(x=-.420, linewidth = 0.5, color = 'b')
#plt.axvline(x=1.420, linewidth = 0.5, color = 'b')

plt.xlim(-5,5)
plt.ylim(0, )
#plt.fill_between(energy, 0, dos, where=(energy < 0), facecolor = 'r', alpha = .25)

#plt.text(.78, 3, 'Fermi Energy' , fontsize = 12, rotation =90)

plt.title('Co hcp Adsorped on Monolayer MoS$_2$ W/ SOC DOS')
plt.savefig('dos_hcp_SOC.png')
plt.show()
