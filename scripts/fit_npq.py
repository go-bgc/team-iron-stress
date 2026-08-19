import pandas as pd
import xarray as xr
import numpy as np
from scipy.optimize import curve_fit

def fit_alpha_npq(ds):

    dsn = ds.copy()

    # calculate npq as difference between fluo_npq and fluo_smooth
    npq = dsn['fluo_npqc']-dsn['fluo_smooth']

    # extract par data
    par = dsn['DOWNWELLING_PAR']

    # select only data where par > 0
    npq = npq.where(par > 0)

    # fit NPQ_max and alpha_NPQ from PAR and NPQ data
    param_opt, pcov = curve_fit(NPQ_func, par, npq)
    # NPQ_max = param_opt[0]
    # alpha_NPQ = param_opt[1]

    dsn = dsn.assign({'npq_max': param_opt[0], 'alpha_npq': param_opt[1]})
    
    return dsn

def npq_func(PAR, NPQ_max, alpha_NPQ):
    return NPQ_max * (1 - np.exp(-(PAR * alpha_NPQ)/NPQ_max))

    
                      
    