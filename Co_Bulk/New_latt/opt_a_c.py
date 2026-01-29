from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import brentq


c = np.array([3.91, 3.92, 3.93, 3.94, 3.95, 3.96, 3.97, 3.98, 3.99, 4.0])

a = np.array([2.44244, 2.4408599, 2.439, 2.43776, 2.436248, 2.43475, 2.43329, 2.43184, 2.43041, 2.429])

slope, intercept = np.polyfit(c,a,1)
x = np.linspace(c[0],c[9], 1000)
y = slope*x + intercept
plt.figure()
plt.plot(x,y)

plt.scatter(c, a)
plt.xlabel("c Lattice Constant")
plt.ylabel("a Lattice Constant")
plt.title("a vs c")
plt.savefig("a_vs_c.png")
plt.show()


# 2) Calculate the optimized lattice parameters from linear fit relationship

volume = 23.414  #optimal volume calculate from EOS to perform root finding method

c_param = np.linspace(c[0],c[9], 1000)
a_relate = slope*c_param + intercept

a_c_vol = (a_relate**2)*c_param


# define f(c)
def f(c):
    a = slope * c + intercept
    return a**2 * c - volume #normalize so that function changes sign

# pick a bracket [c_min, c_max] where f changes sign
c_min, c_max = 3.5, 4.5
c_root = brentq(f, c_min, c_max) # Use Brent's method to find root


plt.figure()
plt.axhline(y=volume)
plt.plot(c_param, a_c_vol)
plt.axvline(x=c_root, ls = 'dashed', c = 'r')
plt.xlabel("c values")
plt.ylabel("Volume Corresponding to c Values")
plt.title("Search for Ideal c")
plt.savefig("ideal_c.png")
plt.show()

# calculate optimal parameters
a_opt = slope*c_root + intercept

# 3) Write a and c out to data file
outfile = f"Opt_a_c.txt"

with open(outfile, "w") as out:
    out.write(f"Ideal Lattice Parameters\nOptimized a: {a_opt} Å\nOptimized c: {c_root} Å")

print(f"Parameters written to {outfile}")


