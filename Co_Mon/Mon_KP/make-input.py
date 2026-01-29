from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword

KP_Values = [27, 28, 29, 30, 31, 32, 33, 34 ,35, 36, 37, 38]

for kp in KP_Values:

    #create Cobalt monolayer
    a = 2.4378
    c = 3.9398
    Cobulk = bulk( 'Co', 'hcp', a = a, c = c)
    mono = hcp0001('Co', size = (1,1,1),  a=a, c=c, vacuum = 10.0,orthogonal = False, periodic = False)

    

    # Create `pwscf` object for `mono`
    pwscf = PWscfInput ( mono )

    #Change the calculation to scf
    update_keyword( pwscf.control.settings, 'calculation', 'scf' )

    update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

    update_keyword( pwscf.control.settings, 'prefix', 'scf' )
    update_keyword( pwscf.control.io, 'disk_io', 'default')
    update_keyword( pwscf.control.io,'wf_collect',False)

    mass = [ 58.933195 ]
    pseudo_potential = [ 'Co.pbe-n-kjpaw_psl.1.0.0.UPF' ]
    update_keyword( pwscf.atomic_species, 'mass', mass )
    update_keyword( pwscf.atomic_species, 'pseudo_potential', pseudo_potential )

    update_keyword( pwscf.system.occupations,'degauss', 0.0073498586)
    update_keyword( pwscf.system.occupations,'smearing','gauss')

    #include vdW corrections
    update_keyword( pwscf.system.occupations,'vdw_corr', 'DFT-D3')
    
    update_keyword( pwscf.kpoints, 'mesh', [kp,kp,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.ecut, 'ecutwfc', 70)
    update_keyword( pwscf.system.ecut, 'ecutrho', 700)
    
    #Convert to string for input file
    kp_str = f"{kp:02d}"
    out_filename = f"scf_kp_{kp_str}.inp"
    write_pwscf_input( pwscf, out_filename)
