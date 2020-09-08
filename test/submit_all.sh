#!/bin/bash

###echo "!!!! WARNING: Submitting for Data!!!!"
echo "!!!! WARNING: Submitting for MC!!!"
python submit_all.py \
  -c runBTagAnalyzer_cfg.py \
  -f CrabDirs/samples.txt \
  -s T2_CH_CERN \
  -p "defaults=PhaseII,runOnData=False" \
  -o "/store/group/upgrade/devdatta/VBF_HH_nonres" \
  -v Phase2_VBFHH

