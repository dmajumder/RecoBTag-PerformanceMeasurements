# RecoBTag-PerformanceMeasurements

This branch is set up to process Phase-2 HLT TDR MiniAOD samples generated in CMSSW_11_1_X:
- /QCD_Pt_600oInf_TuneCP5_14TeV_pythia8/Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1/GEN-SIM-DIGI-RAW-MINIAOD

## Software setup

```
setenv SCRAM_ARCH slc7_amd64_gcc820
cmsrel CMSSW_11_1_3
cd CMSSW_11_1_3/src
cmsenv

setenv CMSSW_GIT_REFERENCE /cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg RecoBTag
git cms-merge-topic dmajumder:BTV_CMSSW_11_1_X_DeepBoosted

git clone -b Phase2_CMWSW_11_1_X --depth 1 https://github.com/dmajumder/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

scram b -j8
```

The ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```

To run on Phase-2 HLT-TDR MiniAOD samples do:
```
cmsRun runBTagAnalyzer_cfg.py defaults=PhaseII runOnData=False maxEvents=500
```
