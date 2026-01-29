from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword


 #create Cobalt monolayer
a = 2.3055
c = a*1.62753
Cobulk = bulk( 'Co', 'hcp', a=a, c = c)
mono = hcp0001('Co', size = (1,1,1), a=a, c=c, vacuum = 7.5,orthogonal = False, periodic = False)

    

# Create `pwscf` object for `mono`
pwscf = PWscfInput ( mono )

#Change the calculation to nscf
update_keyword( pwscf.control.settings, 'calculation', 'scf' )

# Point to relativistic PP directory
update_keyword( pwscf.control.settings, 'pseudo_dir', '/home/antonio/PROJ_MetalTMD/antonio/PSEUDO/' )

update_keyword( pwscf.control.settings, 'prefix', 'pwscf' )
update_keyword( pwscf.control.io, 'disk_io', 'high')
update_keyword( pwscf.control.io,'wf_collect',False)

mass = [ 58.933195 ]
pseudo_potential = [ 'Co.rel-pbe-n-kjpaw_psl.1.0.0.UPF' ]
update_keyword( pwscf.atomic_species, 'mass', mass )
update_keyword( pwscf.atomic_species, 'pseudo_potential', pseudo_potential )

update_keyword( pwscf.system.occupations,'degauss', 0.007)
update_keyword( pwscf.system.occupations,'smearing','fd')

# Update calculation to include total stress
update_keyword( pwscf.control, 'tstress', '.TRUE.' )

# Update system to perform magnetization/SOC calculations
update_keyword( pwscf.system.occupations, 'starting_magnetization', .8)
update_keyword( pwscf.system.occupations, 'noncolin', '.true.')
update_keyword( pwscf.system.occupations, 'lspinorb', '.true.')



update_keyword( pwscf.kpoints, 'mesh', [13,13,1] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.ecut, 'ecutwfc', 65.0)
update_keyword( pwscf.system.ecut, 'ecutrho', 4*65.0)
    
#Convert to string for input file
out_filename = f"scf.inp"
write_pwscf_input( pwscf, out_filename)
