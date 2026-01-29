from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword



#create Cobalt monolayer
a = 2.437815281195015
c = 3.9397986218817924
Cobulk = bulk( 'Co', 'hcp', a=a, c = c)
mono = hcp0001('Co', size = (1,1,1), a=a, c=c, vacuum = 7.5,orthogonal = False, periodic = False)

    

# Create `pwscf` object for `mono`
pwscf = PWscfInput ( mono )

#Change the calculation to scf
update_keyword( pwscf.control.settings, 'calculation', 'nscf' )

update_keyword( pwscf.control.settings, 'pseudo_dir', '/apps/softwares/qe/PP/1.0.0_2019/rel-pbe/PSEUDOPOTENTIALS//' )

update_keyword( pwscf.control.settings, 'prefix', 'scf' )
update_keyword( pwscf.control.io, 'disk_io', 'default')
update_keyword( pwscf.control.io,'wf_collect',False)

mass = [ 58.933195 ]
pseudo_potential = [ 'Co.rel-pbe-n-kjpaw_psl.1.0.0.UPF' ]
update_keyword( pwscf.atomic_species, 'mass', mass )
update_keyword( pwscf.atomic_species, 'pseudo_potential', pseudo_potential )

update_keyword( pwscf.system.occupations,'degauss', 0.0073498586)
update_keyword( pwscf.system.occupations,'smearing','gauss')
update_keyword( pwscf.system.occupations,'vdw_corr', 'DFT-D3')
update_keyword( pwscf.system.occupations,'starting_magnetization',.8)
update_keyword( pwscf.system.occupations,'lspinorb', '.true')
update_keyword( pwscf.system.occupations,'noncolin', '.true')

update_keyword( pwscf.kpoints, 'mesh', [13,13,1] )
update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

update_keyword( pwscf.system.ecut, 'ecutwfc', 70)
update_keyword( pwscf.system.ecut, 'ecutrho', 700)
    
    #Convert to string for input file
out_filename = f"nscf.inp"
write_pwscf_input( pwscf, out_filename)
