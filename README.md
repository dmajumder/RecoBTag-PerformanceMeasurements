# RecoBTag-PerformanceMeasurements

This branch is set up to process Phase-2 HLT TDR MiniAOD samples:
- /VBF_HHTo4B_\*/Phase2HLTTDRWinter20RECOMiniAOD-\*_110X_mcRun4_realistic\*/MINIAODSIM

## Software setup

```
setenv SCRAM_ARCH slc7_amd64_gcc820
cmsrel CMSSW_11_0_0_patch1 
cd CMSSW_11_0_0_patch1/src
cmsenv

setenv CMSSW_GIT_REFERENCE /cvmfs/cms.cern.ch/cmssw.git.daily
git cms-init

git cms-addpkg RecoBTag
git cms-merge-topic emilbols:BTV_11_0_X

git clone -b Phase2_VBFHH --depth 1 https://github.com/dmajumder/RecoBTag-PerformanceMeasurements.git RecoBTag/PerformanceMeasurements

scram b -j8
```

The ntuplizer can be run and configured through ```RecoBTag/PerformanceMeasurements/test/runBTagAnalyzer_cfg.py```

To run on Phase-2 HLT-TDR MiniAOD samples do:
```
cmsRun runBTagAnalyzer_cfg.py defaults=PhaseII runOnData=False maxEvents=500
```
