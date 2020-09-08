#!/usr/bin/env python

from CRABClient.UserUtilities import config
config = config()

from CRABAPI.RawCommand import crabCommand
from httplib import HTTPException

config.General.workArea = 'CrabDirs'
config.General.requestName = 'btagana_phase2'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runBTagAnalyzer_cfg.py'
config.JobType.pyCfgParams = ['defaults=PhaseII', 'runOnData=False']
config.JobType.sendPythonFolder = True
config.JobType.maxJobRuntimeMin = 2630

config.Data.inputDataset = '/VBF_HHTo4B_CV_1_C2V_1_C3_0_TuneCP5_PSWeights_14TeV-madgraph-pythia8/Phase2HLTTDRWinter20RECOMiniAOD-PU200_110X_mcRun4_realistic_v3-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/upgrade/devdatta/VBF_HH_nonres'
config.Data.publication = False
config.Data.outputDatasetTag = 'btagana_phase2_07Sep2020'

config.Site.storageSite = 'T2_CH_CERN'
