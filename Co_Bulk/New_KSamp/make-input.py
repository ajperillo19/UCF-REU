from ase.build import bulk, surface, add_vacuum, hcp0001
from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import math
#k_Values = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]


def next_odd(x):
    n = math.ceil(x)

    return n if n%2 else n+1

for k in range(1,11,1):

    #create Cobalt monolayer
    latt = 2.45
    c = latt*1.62753
    Cobulk = bulk( 'Co', 'hcp', a = latt, c = c)
   

    

    # Create `pwscf` object for `mono`
    pwscf = PWscfInput ( Cobulk )

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


    z_k = 3*k/3.88*2.39

    z = next_odd(z_k)
    update_keyword( pwscf.kpoints, 'mesh', [3*k,3*k,z] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.ecut, 'ecutwfc', 70)
    update_keyword( pwscf.system.ecut, 'ecutrho', 700)
    
    #Convert to string for input file
    k_str = f"{k:02d}"
    out_filename = f"scf_{k_str}.inp"
    write_pwscf_input( pwscf, out_filename)
