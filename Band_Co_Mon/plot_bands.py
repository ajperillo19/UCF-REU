import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


efermi = -2.2796
data = np.loadtxt( 'bands.dat.gnu' )

data_d = np.loadtxt( 'bands_down.dat.gnu')

k = np.unique(data[ :, 0 ])

k_down = np.unique(data[ :, 0])


bands = np.reshape(data[:, 1], (-1, len(k)))

bands_down = np.reshape(data_d[:, 1], (-1,len(k_down)))

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
    plt.plot(k, bands[band, :]-efermi, c='r')

for band in range(len(bands_down)):
    plt.plot(k_down, bands_down[band, :]-efermi, c='b', ls= 'dashed')

# Add labels and title
plt.xlabel('')
plt.ylabel('E - E$_f$ (eV)')
plt.title('Co Monolayer Band Structure')

spin_up_handle   = Line2D([], [], color='red',   marker='o', linestyle='None', label='Spin up')
spin_down_handle = Line2D([], [], color='blue',  marker='o', linestyle='None', label='Spin down')

# Somewhere in your plotting code, after you’ve drawn your data:
plt.legend(handles=[spin_up_handle, spin_down_handle],
           loc='upper right')     # or e.g. 'upper right'
        
# Set axis limits
plt.xlim(gG1, gG2)
plt.ylim(-7.5, 7.5)

# Add label to high-symmetry points
plt.xticks([gG1, K, M, gG2], ['$\Gamma$', 'K', 'M', '$\Gamma$'])

# Hide x-axis minor ticks
plt.tick_params(axis='x', which='minor', bottom = False, top = False)

# Save figure
plt.savefig('plot-bands-Co.png')
plt.show()
