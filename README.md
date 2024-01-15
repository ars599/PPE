# ENSO Metrix from Yann

* https://github.com/CLIVAR-PRP/ENSO_metrics/wiki/Install-using-conda-forge-(recommended)

# PPE analysis and then run the ENSO Merix


# To activate this environment, use
#
#     $ conda activate enso_metrics
#
# To deactivate an active environment, use
#
#     $ conda deactivate

Retrieving notices: ...working... done


# Create XML
Here a .xml file is a link to your data. If I give you one of my files it's not gonna work on your setup.
In the driver I sent I explained how to create your own:
ls /path_to_netcdf_file/file_pattern_for_netcdf_*.nc > /path_to_xml_file/list_files
cdscan -x /path_to_xml_file/file_name_for_xml.xml -f /path_to_xml_file/list_files

# model example:
ls /g/data/p66/ars599/CMIP6/APP_output/CMIP6/CMIP/CSIRO-ARCCSS/ACCESS-CM2/piControl/r3i1p12f1/Amon/ts/gn/v20231104/ts_Amon_ACCESS-CM2_piControl_r3i1p12f1_gn_1* > path_to_xml_file/ts_Amon_piControl_r3i1p12f1_list_files
cdscan -x path_to_xml_file/ts_Amon_piControl_r3i1p12f1.xml -f path_to_xml_file/ts_Amon_piControl_r3i1p12f1_list_files

ls /g/data/p66/ars599/CMIP6/APP_output/CMIP6/CMIP/CSIRO-ARCCSS/ACCESS-CM2/piControl/r1i1p3f1/fx/areacella/gn/v20230517/areacella_fx_ACCESS-CM2_piControl_r1i1p3f1_gn.nc > path_to_xml_file/areacella_fx_piControl_list_files
cdscan -x path_to_xml_file/areacella_fx_piControl.xml -f path_to_xml_file/areacella_fx_piControl_list_files

ls /g/data/p66/ars599/CMIP6/APP_output/CMIP6/CMIP/CSIRO-ARCCSS/ACCESS-CM2/piControl/r1i1p3f1/fx/sftlf/gn/v20230517/sftlf_fx_ACCESS-CM2_piControl_r1i1p3f1_gn.nc > path_to_xml_file/sftlf_fx_piControl_list_files
cdscan -x path_to_xml_file/sftlf_fx_piControl.xml -f path_to_xml_file/sftlf_fx_piControl_list_files


# observation:
 ls /g/data/p66/ars599/obs/month/HadISST_sst.1870-2020.new.nc > path_to_xml_file/sst_Obs_list_files
 cdscan -x path_to_xml_file/sst_Obs.xml -f path_to_xml_file/sst_Obs_list_files


