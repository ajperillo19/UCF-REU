from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2, add_adsorbate
from ase import Atoms


# 1) Build MoS2 single-layer structure
Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)

# 2) Place Co atom @ Molybdenum xy coordinates -- this will assume the hcp hollow arrangement when we repeat structure -- Note: The Molybdenum is placed @ (0,0) xy

ads = add_adsorbate(Mo_S2, 'Co', height = 2.0, position = (0, 0))

### Note: While the object says 'pwscf' this is a relaxation calculation. I simply did not want to go through and replace 'pswcf' with 'relax'    

# Create `pwscf` object for `Mo_S2`
pwscf = PWscfInput ( Mo_S2 )

#Change the calculation to relax
update_keyword( pwscf.control.settings, 'calculation', 'relax' )

update_keyword( pwscf.control.settings, 'pseudo_dir', '/home/antonio/PROJ_MetalTMD/antonio/PSEUDO' )

update_keyword( pwscf.control.settings, 'prefix', 'relax' )
update_keyword( pwscf.control.io, 'disk_io', 'default')
update_keyword( pwscf.control.io,'wf_collect',False)

mass_Mo = 95.94 
pseudo_potential_Mo = 'Mo.rel-pbe-spn-kjpaw_psl.1.0.0.UPF'
mass_S =  32.065
pseudo_potential_S = 'S.rel-pbe-n-kjpaw_psl.1.0.0.UPF'

mass_Co = 58.933195
pseudo_potential_Co = 'Co.rel-pbe-n-kjpaw_psl.1.0.0.UPF'

update_keyword( pwscf.atomic_species, 'mass', [mass_Mo, mass_S, mass_Co] )
update_keyword( pwscf.atomic_species, 'pseudo_potential', [pseudo_potential_Mo, pseudo_potential_S, pseudo_potential_Co] )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')

#Update ion dynamics to Broyden-Fletcher-Goldfarb-Shanno Method: An iterative method for solving unconstrained nonlinear optimization problems -- will provide optimized atomic positions
update_keyword( pwscf.ions, 'ion_dynamics', 'bfgs')


#Update system parameters to perform magnetization calculations
update_keyword( pwscf.system.occupations, 'starting_magnetization(3)', .8)
update_keyword( pwscf.system.occupations, 'noncolin', '.true.')
update_keyword( pwscf.system.occupations, 'lspinorb', '.true.')

update_keyword( pwscf.kpoints, 'mesh', [10,10,1] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.structure, 'nat', 4)
update_keyword( pwscf.system.structure, 'ntyp', 3)
update_keyword( pwscf.system.ecut, 'ecutwfc', 80.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*80.0)
    
#Convert to string for input file
out_filename = f"scf.inp"
write_pwscf_input( pwscf, out_filename)
