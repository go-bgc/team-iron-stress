import pandas as pd
import xarray as xr
import numpy as np
from scipy.optimize import curve_fit

def fit_alpha_npq(ds, npq_tshld=0.1):


    dsn = ds.copy()

    # calculate npq as difference between fluo_npq and fluo_smooth
    npq = dsn['fluo_npqc']-dsn['fluo_smooth']

    # extract par data
    par = dsn['DOWNWELLING_PAR']

    # select only data where above npq depth
    npq = npq()
    par = par()

# Further constraints on the fits 
    # 1. prescribing reasonable maximum bounds for aNPQ and NPQmax (0.1 and 20, respectively)
    # 2. manipulating PAR to yield a zero intercept between NPQ and PAR. This was achieved by subtracting the PAR value where NPQ first reached a low threshold, in this case 0.1.

    # find par value where npq is less than npq threshold
    par_idx = par.where(npq <= npq_tshld).argmin()

    par = par - par(par_idx)
    
    # fit NPQ_max and alpha_NPQ from PAR and NPQ data
    param_opt, pcov = curve_fit(NPQ_func, par, npq)
    # NPQ_max = param_opt[0]
    # alpha_NPQ = param_opt[1]

    dsn = dsn.assign({'npq_max': param_opt[0], 'alpha_npq': param_opt[1]})
    
    return dsn

def npq_func(PAR, NPQ_max, alpha_NPQ):
    return NPQ_max * (1 - np.exp(-(PAR * alpha_NPQ)/NPQ_max))

    
                      
    