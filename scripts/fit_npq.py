import pandas as pd
import xarray as xr
import numpy as np

def fit_alpha_npq(ds0, npq_thr=0.01):

    ds = ds0.copy()

    # calculate npq as difference between fluo_npq and fluo_smooth
    npq = (ds['fluo_npqc']-ds['fluo_smooth'])/ds['fluo_smooth']
    npq = npq.where(~np.isinf(npq),np.nan)
    ds['npq'] = npq

    # Constraint 2: subtract the PAR value where NPQ first reached a low threshold, in this case 0.1.
    par_thr = ds['PRES_ADJUSTED'].where((ds['npq'] < npq_thr) & ~xr.ufuncs.isnan(ds['DOWNWELLING_PAR'])).argmin(dim="N_LEVELS")
    #par_adj = ds['DOWNWELLING_PAR']-par_thr
    
    #par_thr = ds['DOWNWELLING_PAR'].where(npq < npq_thr).min(dim="N_LEVELS")
    #ds['par'] = ds['DOWNWELLING_PAR']-par_thr

    #ds_fit = ds.copy()
    #ds_fit = ds_fit.where(ds_fit['PRES_ADJUSTED'] <= ds_fit['NPQ_depth'])
    par_adj = ds['DOWNWELLING_PAR'].isel(N_LEVELS = par_thr)
    par = ds['DOWNWELLING_PAR'] - par_adj
    par = par.where(par > 0)
    ds['par'] = par
    
    # fit NPQ_max and alpha_NPQ from PAR and NPQ data
    # Constraint 1: prescribe reasonable maximum bounds for aNPQ and NPQmax (0.1 and 20, respectively)
    ds_param = ds['npq'].curvefit(
        coords = ds.par,
        func = npq_func,
        reduce_dims="N_LEVELS",
        bounds={"NPQ_max": (0, 20), "alpha_NPQ": (0, 0.1)},
    )

    ds['NPQ_max'] = ds_param.sel(param='NPQ_max').curvefit_coefficients
    ds['alpha_NPQ'] = ds_param.sel(param='alpha_NPQ').curvefit_coefficients
    
    return ds

def npq_func(PAR, NPQ_max, alpha_NPQ):
    return NPQ_max * (1 - np.exp(-(PAR * alpha_NPQ)/NPQ_max))

    
                      
    