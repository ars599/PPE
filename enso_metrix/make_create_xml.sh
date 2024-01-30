


exp=piControl
idir=/g/data/p66/ars599/CMIP6/APP_output/CMIP6/CMIP/CSIRO-ARCCSS/ACCESS-CM2/$exp/

for run in {12..19}; do
    run=r3i1p${run}f1
    # "taux" "tauy" 
    for var in ts pr hfls hfss rlds rlus rsds rsus; do
        lsFile=${var}_Amon_${exp}_${run}_list_files
        xmlFile=${var}_Amon_${exp}_${run}.xml
        ls $idir/$run/Amon/$var/gn/v*/${var}_Amon_ACCESS-CM2_${exp}_${run}_gn_* > path_to_xml_file/${lsFile}
        cdscan -x path_to_xml_file/${xmlFile} -f path_to_xml_file/${lsFile}
    done
done


