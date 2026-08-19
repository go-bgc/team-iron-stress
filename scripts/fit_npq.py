import pandas as pd
import xarray as xr
import numpy as np
from scipy.optimize import curve_fit

def fit_alpha_npq(ds0, npq_tshld=0.1):

    ds = ds0.copy()

    # calculate npq as difference between fluo_npq and fluo_smooth
    npq = ds['fluo_npqc']-ds['fluo_smooth']

    # select only data where above npq depth
    npq = npq.where(ds['PRES_ADJUSTED'] < ds['NPQ_depth'],drop=True)
    par = ds['DOWNWELLING_PAR'].where(ds['PRES_ADJUSTED'] < ds['NPQ_depth'],drop=True)
    
    # Constraint 2: subtract the PAR value where NPQ first reached a low threshold, in this case 0.1.
    par_idx = par.where(npq < npq_tshld).argmin()
    par = par - par(par_idx)
    
    # fit NPQ_max and alpha_NPQ from PAR and NPQ data
    # Constraint 1: prescribe reasonable maximum bounds for aNPQ and NPQmax (0.1 and 20, respectively)

    param_opt, pcov = curve_fit(NPQ_func, par, npq, bounds=(0, [20., 0.1]))
    # NPQ_max = param_opt[0]
    # alpha_NPQ = param_opt[1]

    ds = ds.assign({'NPQ_MAX': param_opt[0], 'ALPHA_NPQ': param_opt[1]})
    
    return ds

def npq_func(PAR, NPQ_max, alpha_NPQ):
    return NPQ_max * (1 - np.exp(-(PAR * alpha_NPQ)/NPQ_max))

    
                      
    