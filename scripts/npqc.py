import numpy as np
import xarray as xr

def calculate_NPQ_fluo(ds, z_thr = 45):    
    # Calculate NPQ corrected fluorescence following Schallenberg et al. 2022 by setting values
    # to a constant above a threshold depth z_thr (default value 45m). Returns the 17-point smoothed
    # fluorescence profile, chl_smooth, and the NPQ-corrected fluorescence, fluo_npqc
    if not 'CHLA_FLUORESCENCE' in list(ds.variables):
        raise ValueError('Missing fluorescence data')
    if np.isscalar(z_thr):
        z_thr = xr.DataArray(np.full(ds['N_PROF'].shape, z_thr), coords={'N_PROF': ds['N_PROF']})
        
    # Find closest value to z_thr for each profile
    ix_z = (np.abs(ds['PRES_ADJUSTED']-z_thr)).argmin(dim='N_LEVELS')
    
    fluo_smooth = ds['CHLA_FLUORESCENCE'].rolling(N_LEVELS=17, center=True, min_periods=1).median()
    fluo_npqc = fluo_smooth.where(ds['PRES_ADJUSTED'] > z_thr, fluo_smooth.isel(N_LEVELS=ix_z))
    return (fluo_npqc, fluo_smooth)