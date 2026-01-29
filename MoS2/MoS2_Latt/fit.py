import numpy as np
from matplotlib import pyplot as plt
import sympy as sp

# 1) Load Data and retrieve the lattice parameters and energy
data = np.loadtxt('Data_A.txt', skiprows = 1, delimiter = '\t')

latt_params = data[ :, 0]
energies = data[ :, 1]

# 2) Perform 3rd Order Polynomial fit

coefficients = np.polyfit(latt_params, energies, 3)

# 2b) Create 3rd O Polynomial from coefficients

p3 = np.poly1d(coefficients)

# 3) Calculate where derivative is zero to determine least energy lattice constant

a1, a2, a3, a4 = np.polyfit(latt_params, energies, 3)

x_symb = sp.symbols('x')
f = a1*(x_symb**3) + a2*(x_symb**2) + a3*x_symb + a4 

fprime = sp.diff(f,x_symb)
a, b = latt_params[0], latt_params[12]

# Calculate critial points
crit_point = sp.solveset(sp.Eq(fprime,0),x_symb,domain=sp.Interval(a,b))
print("Critial point", crit_point)

# 4) Plot Results
plt. figure()
plt.scatter(latt_params, energies)
x = np.linspace(latt_params[0], latt_params[12], 1000)
fit = p3(x)
plt.plot(x,fit, c='r')
plt.axvline(x=3.168533709742, c = 'gray', ls = '--', lw = 1)
plt.xlabel("Lattice Constant (Å)")
plt.ylabel("Energy (eV)")
plt.title("Energy vs. Lattice Constant w/ p3 Fit")
plt.savefig("MoS2_fit.png")
plt.show()


