from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2, add_adsorbate
from ase.visualize import view
from ase import Atoms

#) Build 2-D MoS2
Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)

# 1) Get Sulfur Positions
pos = Mo_S2.positions

pos_S1_x = pos[1][0]
#print(pos_S1_x)
pos_S1_y = pos[1][1]
#print(pos_S1_y)
pos_S1_z = pos[1][2]
#print(pos_S1_z)


pos_S2_x = pos[2][0]
#print(pos_S2_x)
pos_S2_y = pos[2][1]
#print(pos_S2_y)
pos_S2_z = pos[2][2]
#print(pos_S2_z)

# 2) Add Cobalt Atom at Bridge Site Position

x_bridge = 1.2 +  (pos_S1_x + pos_S2_x) / 2
y_bridge = (pos_S1_y + pos_S2_y) / 2 - 1.2
z_bridge = (pos_S1_z + pos_S2_z) / 2

ads = add_adsorbate(Mo_S2, 'Co', height = 2.0, position = (x_bridge, y_bridge))



### Note: While the object says 'pwscf' this is a relaxation calculation. I simply did not want to go through and replace 'pswcf' with 'relax'    

# Create `pwscf` object for `Mo_S2`
pwscf = PWscfInput ( Mo_S2 )

#Change the calculation to relax
update_keyword( pwscf.control.settings, 'calculation', 'relax' )

update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

update_keyword( pwscf.control.settings, 'prefix', 'relax' )
update_keyword( pwscf.control.io, 'disk_io', 'default')
update_keyword( pwscf.control.io,'wf_collect',False)

mass_Mo = 95.94 
pseudo_potential_Mo = 'Mo.pbe-spn-kjpaw_psl.1.0.0.UPF'
mass_S =  32.065
pseudo_potential_S = 'S.pbe-n-kjpaw_psl.1.0.0.UPF'

mass_Co = 58.933195
pseudo_potential_Co = 'Co.pbe-n-kjpaw_psl.1.0.0.UPF'

update_keyword( pwscf.atomic_species, 'mass', [mass_Mo, mass_S, mass_Co] )
update_keyword( pwscf.atomic_species, 'pseudo_potential', [pseudo_potential_Mo, pseudo_potential_S, pseudo_potential_Co] )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')

#Update ion dynamics to Broyden-Fletcher-Goldfarb-Shanno Method: An iterative method for solving unconstrained nonlinear optimization problems -- will provide optimized atomic positions
update_keyword( pwscf.ions, 'ion_dynamics', 'bfgs')


update_keyword( pwscf.kpoints, 'mesh', [10,10,1] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.structure, 'nat', 4)
update_keyword( pwscf.system.structure, 'ntyp', 3)
update_keyword( pwscf.system.ecut, 'ecutwfc', 80.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*80.0)


#Convert to string for input file
out_filename = f"relax_MoS2_Co.inp"
write_pwscf_input( pwscf, out_filename)
