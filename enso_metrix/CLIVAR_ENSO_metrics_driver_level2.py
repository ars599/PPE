# -*- coding:UTF-8 -*-
# ---------------------------------------------------------------------------------------------------------------------#
# Driver for the CLIVAR ENSO metrics package
# You reached level 2, congratulations!
# Now we will feed many variables to the package
# ---------------------------------------------------------------------------------------------------------------------#




# ---------------------------------------------------------------------------------------------------------------------#
# Import package
# ---------------------------------------------------------------------------------------------------------------------#
import json
# ENSO_metrics package
from EnsoMetrics.EnsoCollectionsLib import defCollection
from EnsoMetrics.EnsoComputeMetricsLib import ComputeCollection
# ---------------------------------------------------------------------------------------------------------------------#




# ---------------------------------------------------------------------------------------------------------------------#
# Parameters
# ---------------------------------------------------------------------------------------------------------------------#
# path where to save data
path_o = "/path/to/output"

# metric collection
mc_name = "ENSO_perf"
# to see all metric collections:
#print(sorted(list(defCollection().keys()), key=lambda v: v.upper()))

# model name (or model and ensemble name, this will we used to properly store the results in the output files)
model_name = "mode_name"

# output json file name (metrics values will be saved in a json file)
fi_js = path_o + "/name_of_the_output_json_file"

# output netCDF file name (dive-down diagnostics, i.e., aditional data to understand the metric value, will be saved in
# a netCDF file)
fi_nc = path_o + "/name_of_the_output_netcdf_file"


# here is an example of a dictionary for IPSL-CM6A-LR, and observational datasets that will be used as a reference to
# evaluate the model
# depending on the metric collection, the package will need some or all these variables
# if the variables are not given for the models or the obs in this dictionary, the related metrics will be skipped
dict_data = {
    "model": {
        "IPSL-CM6A-LR": {
            "lhf": {
                # the CF standard_name is: surface_upward_latent_heat_flux
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_hfls_gr_latest.xml",
                "varname": "hfls",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "lwr": {
                # the CF standard_name is: surface_downwelling_longwave_flux_in_air and surface_upwelling_longwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rlds_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rlus_gr_latest.xml"],
                "varname": ["rlds", "rlus"],
                # the CF standard_name is: cell_area
                # the code is dumb! you need to give areacell/landmask for each variables 
                "path + filename_area": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml"],
                "areaname": ["areacella", "areacella"],
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml"],
                "landmaskname": ["sftlf", "sftlf"],
            },
            "pr": {
                # the CF standard_name is: precipitation_flux
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_pr_gr_latest.xml",
                "varname": "pr",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "shf": {
                # the CF standard_name is: precipitation_flux
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_hfss_gr_latest.xml",
                "varname": "hfss",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "ssh": {
                # the CF standard_name is: precipitation_flux
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Omon_zos_gn_latest.xml",
                "varname": "zos",
                # the CF standard_name is: cell_area
                # ocean grids are often not regular, this file becomes very important!
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacello_gn_latest.xml",
                "areaname": "areacello",
                # variables defined on ocean grid don't have a land-sea mask (or land area fraction)
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "sst": {
                # the CF standard_name is: surface_temperature
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_ts_gr_latest.xml",
                "varname": "ts",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "swr": {
                # the CF standard_name is: surface_downwelling_shortwave_flux_in_air and surface_upwelling_shortwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rsds_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rsus_gr_latest.xml"],
                "varname": ["rsds", "rsus"],
                # the CF standard_name is: cell_area
                # the code is dumb! you need to give areacell/landmask for each variables 
                "path + filename_area": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml"],
                "areaname": ["areacella", "areacella"],
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml"],
                "landmaskname": ["sftlf", "sftlf"],
            },
            "taux": {
                # the CF standard_name is: surface_downward_eastward_stress
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_tauu_gr_latest.xml",
                "varname": "tauu",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "tauy": {
                # the CF standard_name is: surface_downward_eastward_stress
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_tauv_gr_latest.xml",
                "varname": "tauv",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                "landmaskname": "sftlf",
            },
            "thf": {
                # the CF standard_name is: surface_downwelling_shortwave_flux_in_air and surface_upwelling_shortwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_hfls_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_hfss_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rlds_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rlus_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rsds_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_rsus_gr_latest.xml"],
                "varname": ["hfls", "hfss", "rlds", "rlus", "rsds", "rsus"],
                # the CF standard_name is: cell_area
                # the code is dumb! you need to give areacell/landmask for each variables 
                "path + filename_area": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gr_latest.xml"],
                "areaname": ["areacella", "areacella", "areacella", "areacella", "areacella", "areacella"],
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": [
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml",
                    "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr_latest.xml"],
                "landmaskname": ["sftlf", "sftlf", "sftlf", "sftlf", "sftlf", "sftlf"],
            },
        },
    },
    "observations": {
        # GPCPv2.3 downloaded from https://psl.noaa.gov/data/gridded/data.gpcp.html
        "GPCPv2.3": {
            "pr": {
                "path + filename": "/path_to_file/obs_GPCPv2.3_historical_r1i1p1f1_Amon_pr.xml",
                "varname": "pr",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/obs_GPCPv2.3_historical_r1i1p1f1_Amon_lsmask.xml",
                "landmaskname": "lsmask",
            },
        },
        # GODAS downloaded from https://psl.noaa.gov/data/gridded/data.godas.html
        "GODAS": {
            "ssh": {
                "path + filename": "/path_to_file/obs_GODAS_historical_r1i1p1f1_Omon_sshg.xml",
                "varname": "sshg",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "sst": {
                "path + filename": "/path_to_file/obs_GODAS_historical_r1i1p1f1_Omon_sst.xml",
                "varname": "sst",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "taux": {
                "path + filename": "/path_to_file/obs_GODAS_historical_r1i1p1f1_Omon_uflx.xml",
                "varname": "uflx",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "tauy": {
                "path + filename": "/path_to_file/obs_GODAS_historical_r1i1p1f1_Omon_vflx.xml",
                "varname": "vflx",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "thflx": {
                "path + filename": "/path_to_file/obs_GODAS_historical_r1i1p1f1_Omon_thflx.xml",
                "varname": "thflx",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
        },
        # HadISST downloaded from https://www.metoffice.gov.uk/hadobs/hadisst/
        "HadISST": {
            "sst": {
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_sst.xml",
                "varname": "sst",
                # the CF standard_name is: cell_area
                "path + filename_area": None,  
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
        },
        # Tropflux downloaded from https://incois.gov.in/tropflux/
        "Tropflux": {
            "lhf": {
                # the CF standard_name is: surface_upward_latent_heat_flux
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_lhf.xml",
                "varname": "lhf",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname":None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "lwr": {
                # the CF standard_name is: surface_downwelling_longwave_flux_in_air and surface_upwelling_longwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_lwr.xml",
                "varname": "lwr",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "shf": {
                # the CF standard_name is: precipitation_flux
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_shf.xml",
                "varname": "shf",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "sst": {
                # the CF standard_name is: surface_temperature
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_sst.xml",
                "varname": "sst",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "swr": {
                # the CF standard_name is: surface_downwelling_shortwave_flux_in_air and surface_upwelling_shortwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_swr.xml",
                "varname": "swr",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "taux": {
                # the CF standard_name is: surface_downward_eastward_stress
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_taux.xml",
                "varname": "taux",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "tauy": {
                # the CF standard_name is: surface_downward_eastward_stress
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_tauy.xml",
                "varname": "tauy",
                # the CF standard_name is: cell_area
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
            "thf": {
                # the CF standard_name is: surface_downwelling_shortwave_flux_in_air and surface_upwelling_shortwave_flux_in_air
                # they need to be listed in this order!
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_netflux.xml",
                "varname": "netflux",
                # the CF standard_name is: cell_area
                # the code is dumb! you need to give areacell/landmask for each variables 
                "path + filename_area": None,
                "areaname": None,
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": None,
                "landmaskname": None,
            },
        },
    },
}

# variables have a nickname in the code:
#   lhf: Surface Latent Heat Flux (upward or downward), in CMIP this corresponds to hfls
#   lwr: Net Surface Downward Longwave Radiation, in CMIP this corresponds to rlds - rlus
#   pr: precipitation, in CMIP this corresponds to pr
#   shf: Surface Sensible Heat Flux (upward or downward), in CMIP this corresponds to hfss
#   ssh: Sea Surface Height Above Geoid, in CMIP this corresponds to zos
#   sst: Sea Surface Temperature, in CMIP this corresponds to ts
#   swr: Net Surface Downward Shortwave Radiation, in CMIP this corresponds to rsds - rsus
#   taux: Surface Downward Eastward Wind Stress, in CMIP this corresponds to tauu
#   tauy: Surface Downward Northward Wind Stress, in CMIP this corresponds to tauv
#   thf: Net Surface Downward Heat Flux, in CMIP this corresponds to hfls + hfss + rlds - rlus + rsds - rsus

# Note that the CMIP / observations computation of the fluxes is hard codded in the package
# If your data does not match the way it is codded in the package, you need to adapt the function
# ReferenceObservations in lib/EnsoCollectionsLib.py (for observation)
# CmipVariables in lib/EnsoCollectionsLib.py (for models)
# You can also add observation datasets in ReferenceObservations if they are not codded
# ---------------------------------------------------------------------------------------------------------------------#




# ---------------------------------------------------------------------------------------------------------------------#
# Main
# ---------------------------------------------------------------------------------------------------------------------#
# Compute metric collection
# Note that the epoch used to compute the metric is defined in the metric collection, but you can override it!
# observed_fyear is the first year used for observational dataset
# observed_lyear is the last year used for observational dataset
# so the package will try to read the observations within the intervall [observed_fyear, observed_lyear], a shorter
# period will be read if a shorter period is available. The code will only keep full years (from Jan to Dec)
# the same applies for model data (modeled_fyear, modeled_lyear)
# e.g.:
dict_o, _ = ComputeCollection(mc_name, dict_data, model_name, netcdf=True, netcdf_name=fi_nc, observed_fyear=1980,
    observed_lyear=2009, modeled_fyear=1850, modeled_lyear=1879)
# save as json file
if ".json" not in fi_js:
    fi_js += ".json"
with open(fi_js, "w") as outfile:
    json.dump({model_name: dict_o}, outfile, sort_keys=True)
# ---------------------------------------------------------------------------------------------------------------------#


