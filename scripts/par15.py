# code to find par = 15 
def par15(ds):
    
    
    par15_pressure = np.full(ds.sizes['N_PROF'], np.nan) # may need to change from time. 
    profiles = range(ds.sizes['N_PROF']) # define profile range 

    for p in profiles:

        par = ds['DOWNWELLING_PAR'][p,:].values # make 
        pres = ds['PRES_ADJUSTED'][p,:].values
    
        par_value_check = par >= 14
        par = par[par_value_check] # check that is large (avoid weird small or 0 values) 
        pres = pres[par_value_check] 
    
        valid = np.isfinite(par) & np.isfinite(pres) # make sure a value legth 
        par = par[valid]
        press = pres[valid] 
        
        
        if len(par) == 0:
            continue # if 0, move on 

        find_par_15 = np.abs(par - 15).argmin()
        
        
        # Save pressure
        par15_pressure[p] = press[find_par_15] # Save pressure

    
    ds['par_15_pressure'] = (['N_PROF'], par15_pressure)# Add result to dataset
    return argo_n