import numpy as np
import xarray as xr


def calculate_NPQ_depth(ds0): 
    ds = ds0.copy()
    ml09 = ds['ml_depth']*.9
    npq_depth = (ml09).where(ml09 < ds['par_depth'], ds['par_depth'])

    ds = ds.assign({'NPQ_depth': npq_depth})
    return ds

def calculate_NPQ_fluo(ds0, *, z_thr = 45):    
    # Calculate NPQ corrected fluorescence following Schallenberg et al. 2022 by setting values
    # to a constant above a threshold depth z_thr (default value 45m). Returns the 17-point smoothed
    # fluorescence profile, chl_smooth, and the NPQ-corrected fluorescence, fluo_npqc
    ds = ds0.copy()
    if not 'CHLA_FLUORESCENCE' in list(ds.variables):
        raise ValueError('Missing fluorescence data')
    if all([x in list(ds.variables) for x in ['ml_depth', 'par_depth']]):
        ds = calculate_NPQ_depth(ds)
    elif np.isscalar(z_thr):
        ds['NPQ_depth'] = xr.DataArray(np.full(ds['N_PROF'].shape, z_thr), coords={'N_PROF': ds['N_PROF']})
        
    # Find closest value to z_thr for each profile
    ix_z = (np.abs(ds['PRES_ADJUSTED']-ds['NPQ_depth'])).argmin(dim='N_LEVELS')
    
    fluo_smooth = ds['CHLA_FLUORESCENCE'].rolling(N_LEVELS=17, center=True, min_periods=1).median()
    fluo_npqc = fluo_smooth.where(ds['PRES_ADJUSTED'] > ds['NPQ_depth'], fluo_smooth.isel(N_LEVELS=ix_z))

    ds = ds.assign({'fluo_smooth': fluo_smooth, 'fluo_npqc': fluo_npqc})
    
    return ds
