from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2, add_adsorbate
from ase import Atoms
from ase.io import read, write
from ase.io.espresso import read_espresso_out


# 1) We are going to perform an scf calculation for our relaxed hcp (most stable) adsorption configuration -- we want to make sure the total stress of the system ~ 0

#) Read QE output file for hcp relaxation
atoms = read("rel_hcp_fix.out")
    
# Create `pwscf` object for `Mo_S2`
pwscf = PWscfInput ( atoms )

#Change the calculation to nscf
update_keyword( pwscf.control.settings, 'calculation', 'nscf' )

# Point to relativistic PP directory
update_keyword( pwscf.control.settings, 'pseudo_dir', '/home/antonio/PROJ_MetalTMD/antonio/PSEUDO' )

update_keyword( pwscf.control.settings, 'prefix', 'pwscf' )
update_keyword( pwscf.control.io, 'disk_io', 'high')
update_keyword( pwscf.control.io,'wf_collect',False)
update_keyword( pwscf.control, 'outdir', './tmp/')

# Update calculation to include total stress
update_keyword( pwscf.control, 'tstress', '.TRUE.' )


# Update PP for full relativistic
mass_Mo = 95.94 
pseudo_potential_Mo = 'Mo.rel-pbe-spn-kjpaw_psl.1.0.0.UPF'
mass_S =  32.065
pseudo_potential_S = 'S.rel-pbe-n-kjpaw_psl.1.0.0.UPF'

mass_Co = 58.933195
pseudo_potential_Co = 'Co.rel-pbe-spn-kjpaw_psl.1.0.0.UPF'

update_keyword( pwscf.atomic_species, 'mass', [mass_Mo, mass_S, mass_Co] )
update_keyword( pwscf.atomic_species, 'pseudo_potential', [pseudo_potential_Mo, pseudo_potential_S, pseudo_potential_Co] )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')

#Update ion dynamics to Broyden-Fletcher-Goldfarb-Shanno Method: An iterative method for solving unconstrained nonlinear optimization problems -- will provide optimized atomic positions
#update_keyword( pwscf.ions, 'ion_dynamics', 'bfgs')


#Update system parameters to perform magnetization calculations
update_keyword( pwscf.system.occupations, 'starting_magnetization(3)', .8)
#update_keyword( pwscf.system.occupations, 'nspin', 2)

update_keyword( pwscf.kpoints, 'mesh', [100,100,1] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.structure, 'nat', 4)
update_keyword( pwscf.system.structure, 'ntyp', 3)
update_keyword( pwscf.system.ecut, 'ecutwfc', 80.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*80.0)



# Update system card to include noncollinear spin
update_keyword( pwscf.system.occupations, 'noncolin', '.true.')
update_keyword( pwscf.system.occupations, 'lspinorb', '.true.')


#Convert to string for input file
out_filename = f"nscf.inp"
write_pwscf_input( pwscf, out_filename)
