from ase.eos import calculate_eos
from ase.eos import EquationOfState
from ase.units import kJ
import numpy as np

# 1) Load Data and retrieve the lattice parameters and energy
data = np.loadtxt('summary.csv', skiprows = 1, delimiter = ',', usecols=(1,2))

volumes = data[ :, 0]
energies = data[ :, 1]

# 2) Perform EOS fitting calculation using ASE Libraries
#volumes = 4.0*latt_params**2
eos = EquationOfState(volumes, energies)

v0, e0, B = eos.fit()

#2b) Compute the optimizes lattice constant from EOS volume
a0 = np.sqrt(v0/4.0)

#Convert Bulk Modulus to SI units
B_GPa = B / kJ *1.0e24

eos.plot('Co_EOS.png')
#Convert all values into strings to be written out to a text file
B_GPa_str = str(B_GPa)
v0_str = str(v0)
e0_str = str(e0)
a0_str = str(a0)

# Pack into a dictionary for efficiency
params = {
    "Optimal Volume (Å³)"          : v0_str,
    "Total Energy (eV)"            : e0_str,
    "Bulk Modulus (GPa)"           : B_GPa_str,
    "Optimal lattice constant (Å)" : a0_str,
}

# Write to text file
#with open("C10Optml_params.txt", "w") as out:
    
 #   for key, val in params.items():
 #       out.write(f"{key}: {val}\n")
#print('Optimal parameters written to: C10Optml_params.txt')
