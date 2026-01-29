from dlePy.vasp.kpoints import vasp_band_gen_k

klist=(
   ( 0.0, 0.0, 0.0 ), #Gamma
   ( 0.5,  0.0, 0.0 ), #M
   ( 1/3, 1/3, 0.0 ), #K
   ( 0.0, 0.0, 0.0 ), # Gamma
   )
    
npts = ppf = 100

vasp_band_gen_k(klist,npts,ppf)


