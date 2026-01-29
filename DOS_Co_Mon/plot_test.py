import matplotlib.pyplot as plt
import numpy as np

# List of DOS files and corresponding labels
files = ['dos_36.dat', 'dos_48.dat', 'dos_60.dat', 'dos_72.dat']
labels = ['36x36', '48x48', '60x60', '72x72']

efermi = -2.150

# Set up the figure
plt.figure(figsize=(8, 6))

# Choose a colormap
cmap = plt.get_cmap('viridis')
colors = [cmap(i / (len(files) - 1)) for i in range(len(files))]

# Loop through files
for fname, label, color in zip(files, labels, colors):
    energy, dos_up, dos_down, idos = np.loadtxt(fname, unpack=True)
    plt.plot(energy - efermi, dos_up, linewidth=2, color=color, label=f'{label} (up)')
    plt.plot(energy - efermi, -dos_down, linewidth=2, linestyle='--', color=color, label=f'{label} (down)')

# Formatting
plt.axhline(y=0, linewidth=0.5, color='k')
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlabel('E - E$_f$ (eV)')
plt.ylabel('Density of States (state/eV)')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title('Monolayer Co DOS Comparison')
plt.legend(loc='upper right', fontsize='small')
plt.tight_layout()

# Save and show
plt.savefig('dos_Co_Mon_comparison.png', dpi=300)
plt.show()

