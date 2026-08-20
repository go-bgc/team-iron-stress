import numpy as np
import gsw
import xarray as xr

#calculate MLD for profiles
def mld_calc(floatdata):
    MLD=np.zeros(len(floatdata.N_PROF))
    MLD[:]=np.nan
    for i in floatdata.N_PROF:
        prof=floatdata.isel(N_PROF=i)
        densprof=gsw.density.sigma0(prof.PSAL,prof.TEMP).values
        # refdens=densprof[np.abs(prof.PRES - 15).argmin()]
        refdep=np.abs(prof.PRES - 10).argmin()
        refdens=np.mean(densprof[0:refdep.values])
        for g in range(refdep.values,len(densprof)):
            dens=densprof[g]
            densdiff=np.abs(refdens-dens)
            if densdiff>0.03:
                MLD[i]=prof.isel(N_LEVELS=g).PRES
                break
    ds = floatdata.copy()
    ds = ds.assign({'ml_depth': xr.DataArray(MLD, coords={'N_PROF': ds['N_PROF']})})
    return(ds)