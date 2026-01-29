from dlePy.vasp.kpoints import vasp_band_gen_k

klist=(
   ( 0.0, 0.0, 0.0 ), #Gamma
   ( 0.5,  0.0, 0.0 ), #M
   ( 0.3333333333333333, 0.3333333333333333, 0.0 ), #K
   ( 0.0, 0.0, 0.0 ), # Gamma
   )
    
npts = ppf = 100

vasp_band_gen_k(klist,npts,ppf)


