from matplotlib import pyplot as plt
import numpy as np

def find_intersection(m1, c1, m2, c2):
    x = (c2-c1)/(m1-m2)
    y = m1*x +c1
    return(x,y)

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

volume = 23.414 #optimized volume calculate from EOS

c_param = np.linspace(c[0],c[9], 1000)
a_relate = slope*c_param + intercept

a_c_vol = (a_relate**2)*c_param

a_opt = slope*3.93979 + intercept
print(f"Optimal c: 3.93979 Å \nOptimal a: {a_opt} Å")

plt.figure()
plt.axhline(y=volume)
plt.plot(c_param, a_c_vol)
plt.axvline(x=3.93979)
plt.xlabel("c values")
plt.ylabel("Volume Corresponding to c Values")
plt.title("Search for Ideal c")
plt.savefig("ideal_c.png")
plt.show()



