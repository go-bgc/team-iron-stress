import pandas as pd
import xarray as xr
import numpy as np
from scipy.optimize import curve_fit

def fit_alpha_npq(prof_data):

    # NPQ = NPQ_max(1 - exp(-(PAR * alpha_NPQ) / NPQ_max))
    # fit NPQ_max and alpha_NPQ from PAR and NPQ data
    param_opt, pcov = curve_fit(NPQ_func, prof_data.PAR, prof_data.NPQ)
    # NPQ_max = param_opt[0]
    # alpha_NPQ = param_opt[1]
    return param_opt

def npq_func(PAR, NPQ_max, alpha_NPQ):
    return NPQ_max * (1 - np.exp(-(PAR * alpha_NPQ)/NPQ_max)

                      
    