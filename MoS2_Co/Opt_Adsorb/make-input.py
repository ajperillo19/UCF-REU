from dlePy.qe.pwscf import PWscfInput, write_pwscf_input, update_keyword
import ase.build
from ase.build import mx2, add_adsorbate
from ase.visualize import view
from ase import Atoms
from ase.io import read, write
from ase.io.espresso import read_espresso_out


KP_Values = [9, 12, 15, 18, 21, 24]

Mo_S2 = ase.io.read('rel_opt.out')

ads = add_adsorbate(Mo_S2, 'Co', height = 2.0, position = (0, 0))

for kp in KP_Values:

    # Create `pwscf` object for `Mo_S2`
    pwscf = PWscfInput ( Mo_S2 )

    #Change the calculation to scf
    update_keyword( pwscf.control.settings, 'calculation', 'scf' )

    update_keyword( pwscf.control.settings, 'pseudo_dir', '/shared/ESPRESSO/PSLIBRARY/1.0.0/pbe/PSEUDOPOTENTIALS/' )

    update_keyword( pwscf.control.settings, 'prefix', 'scf' )
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

    update_keyword( pwscf.system.occupations,'degauss', 0.0073498586)
    update_keyword( pwscf.system.occupations,'smearing','gauss')
    

    #Update system parameters to perform magnetization calculations
    update_keyword( pwscf.system.occupations, 'starting_magnetization(3)', .8)
    update_keyword( pwscf.system.occupations, 'nspin', 2)

    #Include vdW corrections
    update_keyword( pwscf.system.occupations, 'vdw_corr', 'DFT-D3')
    
    update_keyword( pwscf.kpoints, 'mesh', [kp,kp,1] )
    update_keyword( pwscf.kpoints, 'smesh',[0,0,0] )

    update_keyword( pwscf.system.structure, 'nat', 4)
    update_keyword( pwscf.system.structure, 'ntyp', 3)
    update_keyword( pwscf.system.ecut, 'ecutwfc', 70.0)
    update_keyword( pwscf.system.ecut, 'ecutrho', 700)
    
    #Convert to string for input file
    kp_str = f"{kp:02d}"
    out_filename = f"scf_kp_{kp_str}.inp"
    write_pwscf_input( pwscf, out_filename)
