from ase import Atoms
from ase.build import bulk
from ase.visualize import view 
from ase.visualize.plot import plot_atoms
import matplotlib.pyplot as plt

a = 2.47

c = 4.02

Cobulk =  bulk('Co',crystalstructure='hcp',a=a,c= c)

view(Cobulk)






