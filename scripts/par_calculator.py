import numpy as np
import xarray as xr
from par_bgc_argo_pitarch import par_from_Ed_380_443_490_555_v5

def calculate_par(ds):
    ds['PRES_ADJUSTED'].dims
    z = ds['PRES_ADJUSTED'].stack(N_POINTS=("N_PROF", "N_LEVELS"))

    Ed = ds[['DOWN_IRRADIANCE380','DOWN_IRRADIANCE443','DOWN_IRRADIANCE490','DOWN_IRRADIANCE555']]   
    Ed = Ed.to_array(dim='variable')
    Ed = Ed.stack(N_POINTS=("N_PROF", "N_LEVELS"))
    Ed = Ed.T

    PAR= par_from_Ed_380_443_490_555_v5.PAR_from_Ed_380_443_490_555_v5(Ed.values,z.values)
    
    PAR_CALCULATED = xr.DataArray(PAR[0], coords=z.coords)
    PAR_CALCULATED = PAR_CALCULATED.unstack()
    ds['DOWNWELLING_PAR'] = PAR_CALCULATED
    return ds
    