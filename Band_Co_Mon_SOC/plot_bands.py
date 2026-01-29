import numpy as np
import matplotlib.pyplot as plt


efermi = -2.1401
data = np.loadtxt( 'bands.dat.gnu' )

k = np.unique(data[ :, 0 ])


bands = np.reshape(data[:, 1], (-1, len(k)))

# Set high-symmetry points
gG1 = k[0]
M   = k[37]
K   = k[53]
gG2 = k[99]

#Create figure object
plt.figure()
# Plot dotted line at Fermi energy
plt.axhline(0, c='gray', ls=':')

# Plot dotted lines at high-symmetry points
plt.axvline(K, c='gray')
plt.axvline(M, c='gray')


#plt.axhline(y=.91, c='r')
#plt.axhline(y=-.84, c='r')

# Plot band structure
for band in range(len(bands)):
    plt.plot(k, bands[band, :]-efermi, c='b')

# Add labels and title
plt.xlabel('')
plt.ylabel('E - E$_f$ (eV)')
plt.title('Co Monolayer Band Structure With SOC')

# Set axis limits
plt.xlim(gG1, gG2)
plt.ylim(-7.5, 7.5)

# Add label to high-symmetry points
plt.xticks([gG1, K, M, gG2], ['$\Gamma$', 'K', 'M', '$\Gamma$'])

# Hide x-axis minor ticks
plt.tick_params(axis='x', which='minor', bottom = False, top = False)

# Save figure
plt.savefig('plot-bands-Co-SOC.png')
plt.show()
