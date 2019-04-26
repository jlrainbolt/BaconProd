import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as vp
import os

process = cms.Process('MakingBacon')

is_data_flag  = False                                       # flag for if process data
do_hlt_filter = False                                       # flag to skip events that fail relevant triggers
hlt_filename  = "BaconAna/DataFormats/data/HLTFile_25ns"    # list of relevant triggers

cmssw_base = os.environ['CMSSW_BASE']
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
if not is_data_flag:
    process.GlobalTag.globaltag = cms.string('102X_upgrade2018_realistic_v18')

#--------------------------------------------------------------------------------
# Default options
#================================================================================
options = vp.VarParsing ('analysis')
options.maxEvents   = 15000
options.inputFiles  = '/store/mc/RunIIAutumn18MiniAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/80000/FFDCFC59-4ABE-0646-AABE-BD5D65301169.root')
options.parseArguments()

#--------------------------------------------------------------------------------
# Import of standard configurations
#================================================================================
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryDB_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('TrackingTools/TransientTrack/TransientTrackBuilder_cfi')

#--------------------------------------------------------------------------------
# Import custom configurations
#================================================================================
# Egamma post-reco corrections
#   (https://twiki.cern.ch/twiki/bin/view/CMS/EgammaPostRecoRecipes)
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process,
        runEnergyCorrections=True,  # preliminary 2018 electron energy corrections
        runVID=True,                # get Fall17V2 IDs, which "breaks" photons
        era='2018-Prompt')

#--------------------------------------------------------------------------------
# Input settings
#================================================================================
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(options.inputFiles))
process.source.inputCommands = cms.untracked.vstring("keep *", "drop *_MEtoEDMConverter_*_*")

#--------------------------------------------------------------------------------
# Reporting
#================================================================================
process.MessageLogger.cerr.FwkReport.reportEvery = 10
process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(False),
        Rethrow     = cms.untracked.vstring('ProductNotFound'),
        fileMode    = cms.untracked.string('NOMERGE'),
        )

#--------------------------------------------------------------------------------
# Bacon making settings
#================================================================================
process.ntupler = cms.EDAnalyzer('NtuplerMod',
        skipOnHLTFail       = cms.untracked.bool(do_hlt_filter),
        useTrigger          = cms.untracked.bool(True),
        TriggerObject       = cms.untracked.string("slimmedPatTrigger"),
        TriggerFile         = cms.untracked.string(hlt_filename),
        useAOD              = cms.untracked.bool(False),
        outputName          = cms.untracked.string('Output.root'),
        edmPVName           = cms.untracked.string('offlineSlimmedPrimaryVertices'),
        edmGenRunInfoName   = cms.untracked.string('generator'),

        Info = cms.untracked.PSet(
                isActive            = cms.untracked.bool(True),
                edmPFCandName       = cms.untracked.string('packedPFCandidates'),
                edmPileupInfoName   = cms.untracked.string('slimmedAddPileupInfo'),
                edmBeamspotName     = cms.untracked.string('offlineBeamSpot'),
                edmMETName          = cms.untracked.string('slimmedMETs'),
                edmPFMETName        = cms.untracked.InputTag('slimmedMETsV2','','MakingBacon'),
                edmMVAMETName       = cms.untracked.string(''),
                edmPuppETName       = cms.untracked.InputTag('slimmedMETsPuppi','','MakingBacon'),
                edmRhoForIsoName    = cms.untracked.string('fixedGridRhoFastjetAll'),
                edmRhoForJetEnergy  = cms.untracked.string('fixedGridRhoFastjetAll'),
                doFillMETFilters    = cms.untracked.bool(False),
                doFillMET           = cms.untracked.bool(False),
                ecalWeightName      = cms.untracked.InputTag('prefiringweight:NonPrefiringProb'),
                ecalWeightUpName    = cms.untracked.InputTag('prefiringweight:NonPrefiringProbUp'),
                ecalWeightDownName  = cms.untracked.InputTag('prefiringweight:NonPrefiringProbDown'),
                ),

        GenInfo = cms.untracked.PSet(
                isActive            = ( cms.untracked.bool(False) if is_data_flag else cms.untracked.bool(True) ),
                edmGenEventInfoName = cms.untracked.string('generator'),
                edmGenParticlesName = cms.untracked.string('prunedGenParticles'),
                edmGenPackParticlesName = cms.untracked.string('packedGenParticles'),
                fillAllGen          = cms.untracked.bool(True),
                fillLHEWeights      = cms.untracked.bool(True)
                ),

        PV = cms.untracked.PSet(
                isActive        = cms.untracked.bool(True), 
                edmName         = cms.untracked.string('offlineSlimmedPrimaryVertices'),
                minNTracksFit   = cms.untracked.uint32(0),
                minNdof         = cms.untracked.double(4),
                maxAbsZ         = cms.untracked.double(24),
                maxRho          = cms.untracked.double(2)
                ),

        Electron = cms.untracked.PSet(
                isActive                  = cms.untracked.bool(True),
                minPt                     = cms.untracked.double(6.9),
                edmName                   = cms.untracked.string('slimmedElectrons'),
                edmSCName                 = cms.untracked.InputTag('reducedEgamma','reducedSuperClusters'),
                edmPuppiName              = cms.untracked.string('puppi'),
                edmPuppiNoLepName         = cms.untracked.string('puppiNoLep'),
                usePuppi                  = cms.untracked.bool(False),
                useTriggerObject          = cms.untracked.bool(True),
                edmEcalPFClusterIsoMapTag = cms.untracked.InputTag('electronEcalPFClusterIsolationProducer'),
                edmHcalPFClusterIsoMapTag = cms.untracked.InputTag('electronHcalPFClusterIsolationProducer'),
                fillVertices              = cms.untracked.bool(False)
                ),

        Muon = cms.untracked.PSet(
                isActive                  = cms.untracked.bool(True),
                minPt                     = cms.untracked.double(4.9),
                edmName                   = cms.untracked.string('slimmedMuons'),
                edmPuppiName              = cms.untracked.string('puppi'),
                edmPuppiNoLepName         = cms.untracked.string('puppiNoLep'),
                usePuppi                  = cms.untracked.bool(False),    
                fillVertices              = cms.untracked.bool(False),
                useTriggerObject          = cms.untracked.bool(True),
                ),
        )

process.baconSequence = cms.Sequence(
        process.egammaPostRecoSeq           *
        process.ntupler
        )

#--------------------------------------------------------------------------------
# apply trigger filter, if necessary
#================================================================================
if do_hlt_filter:
    process.load('HLTrigger/HLTfilters/hltHighLevel_cfi')
    process.hltHighLevel.throw = cms.bool(False)
    process.hltHighLevel.HLTPaths = cms.vstring()
    hlt_file = open(cmssw_base + "/src/" + hlt_filename, "r")
    for line in hlt_file.readlines():
        line = line.strip()              # strip preceding and trailing whitespaces
        if (line[0:3] == 'HLT'):         # assumes typical lines begin with HLT path name (e.g. HLT_Mu15_v1)
            hlt_path = line.split()[0]
            process.hltHighLevel.HLTPaths.extend(cms.untracked.vstring(hlt_path))
    process.p = cms.EndPath(process.hltHighLevel*process.baconSequence)
else:
    process.p = cms.EndPath(process.baconSequence)
