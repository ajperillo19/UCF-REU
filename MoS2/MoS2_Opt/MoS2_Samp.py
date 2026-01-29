from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2, add_adsorbate
from ase.visualize import view
from ase import Atoms

#) Build 2-D MoS2
Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)

view(Mo_S2)
