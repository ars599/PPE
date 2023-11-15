# -*- coding:UTF-8 -*-
# ---------------------------------------------------------------------------------------------------------------------#
# Driver for the CLIVAR ENSO metrics package
# You need to feed data to the code, then everything is done for you
# This is your first step to run the package
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

# the most difficult part is here!
# the package needs to know where to find the data!
# you need to create a dictionary with the variables, and each variable needs to be in a single file. Usually data
# storage servers create a link towards the data using an xml file
# if you have to do it, you can do it in the terminal:
#ls /path_to_netcdf_file/file_pattern_for_netcdf_*.nc > /path_to_xml_file/list_files
#cdscan -x /path_to_xml_file/file_name_for_xml.xml -f /path_to_xml_file/list_files

# here is an example of a dictionary for the surface temperature of IPSL-CM6A-LR, and observational dataset that will be
# used as a reference to evaluate the model
# the following keywords are recognized by the package and need to be in the dictionary: "model", "observations", "sst",
#   "path + filename", "varname", "path + filename_area", "areaname", "path + filename_landmask", "landmaskname"
dict_data = {
    "model": {
        "IPSL-CM6A-LR": {
            "sst": { # pr sst ts ssh 
                # the CF standard_name is: surface_temperature
                "path + filename": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_Amon_ts_gr_latest.xml",
                "varname": "ts",
                # the CF standard_name is: cell_area
                "path + filename_area": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_areacella_gn_latest.xml",
                "areaname": "areacella",
                # the CF standard_name is: land_area_fraction
                "path + filename_landmask": "/path_to_file/CMIP6_IPSL_IPSL-CM6A-LR_historical_r1i1p1f1_fx_sftlf_gr1_latest.xml",
                "landmaskname": "sftlf",
            },
        },
    },
    "observations": {
        # HadISST downloaded from https://www.metoffice.gov.uk/hadobs/hadisst/
        "HadISST": {
            "sst": {
                "path + filename": "/path_to_file/obs_HadISST_historical_r1i1p1f1_Omon_sst.xml",
                "varname": "sst",
                # the area of each grid cell is not available for HadISST so set this to None. HadISST is defined on a
                # regular grid so the package will be able to compute it, this is not a problem
                "path + filename_area": None,  
                "areaname": None,
                # the land-sea mask (or land area fraction) is not available for HadISST so set this to None. HadISST is
                # defined only over open ocean so only sst is available, this is not a problem
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

# heat fluxes are tricky to feed to the package and the way to sum them is hard codded in the package
# we will deal with that in another example
# ---------------------------------------------------------------------------------------------------------------------#




# ---------------------------------------------------------------------------------------------------------------------#
# Main
# ---------------------------------------------------------------------------------------------------------------------#
# Compute metric collection
dict_o, _ = ComputeCollection(mc_name, dict_data, model_name, netcdf=True, netcdf_name=fi_nc)
# save as json file
if ".json" not in fi_js:
    fi_js += ".json"
with open(fi_js, "w") as outfile:
    json.dump({model_name: dict_o}, outfile, sort_keys=True)
# ---------------------------------------------------------------------------------------------------------------------#


