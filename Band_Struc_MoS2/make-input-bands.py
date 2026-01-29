from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2
from ase.visualize import view
from ase import Atoms

#) Build 2-D MoS2
Mo_S2 = mx2(formula = 'MoS2', kind = '2H', a = 3.1685, thickness = 3.19, size = (1,1,1), vacuum = 7.5)


# We will be performing an scf calculation to get the charge density which will be used for our electronic band structure calculations    

# Create `pwscf` object for `Mo_S2`
pwscf = PWscfInput ( Mo_S2 )

#Change the calculation to bands
update_keyword( pwscf.control.settings, 'calculation', 'bands' )

update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

update_keyword( pwscf.control.settings, 'prefix', 'pwscf' )
update_keyword( pwscf.control.io, 'disk_io', 'high')
update_keyword( pwscf.control.io,'wf_collect',False)

update_keyword( pwscf.control.io, 'outdir', './tmp/')

update_keyword( pwscf.control, 'tstress', '.TRUE.')

mass_Mo = 95.94 
pseudo_potential_Mo = 'Mo.pbe-spn-kjpaw_psl.1.0.0.UPF'
mass_S =  32.065
pseudo_potential_S = 'S.pbe-n-kjpaw_psl.1.0.0.UPF'


update_keyword( pwscf.atomic_species, 'mass', [mass_Mo, mass_S ] )
update_keyword( pwscf.atomic_species, 'pseudo_potential', [pseudo_potential_Mo, pseudo_potential_S] )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')

#Update ion dynamics to Broyden-Fletcher-Goldfarb-Shanno Method: An iterative method for solving unconstrained nonlinear optimization problems -- will provide optimized atomic positions
update_keyword( pwscf.ions, 'ion_dynamics', 'bfgs')


#update_keyword( pwscf.kpoints, 'mesh', [10,10,1] )
#update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.structure, 'nat', 3)
update_keyword( pwscf.system.structure, 'ntyp', 2)
update_keyword( pwscf.system.ecut, 'ecutwfc', 80.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*80.0)


#Convert to string for input file
out_filename = f"nscf.inp"
write_pwscf_input( pwscf, out_filename)
