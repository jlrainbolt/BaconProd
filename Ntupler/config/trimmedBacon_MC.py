import FWCore.ParameterSet.Config as cms
import os

process = cms.Process('MakingBacon')

is_data_flag  = False                                       # flag for if process data
do_hlt_filter = False                                       # flag to skip events that fail relevant triggers
hlt_filename  = "BaconAna/DataFormats/data/HLTFile_25ns"    # list of relevant triggers

cmssw_base = os.environ['CMSSW_BASE']
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
if is_data_flag:
    process.GlobalTag.globaltag = cms.string('94X_dataRun2_v10')
else:
    process.GlobalTag.globaltag = cms.string('94X_mcRun2_asymptotic_v3')

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
        runEnergyCorrections=False,  # corrections by default are fine for 2016 legacy
        runVID=True,                 # get Fall17V2 IDs, which "breaks" photons
        era='2016-Legacy')  

# Level 1 ECAL prefiring fix
#   (https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe)
#   Needs old-style (i.e. not post-VID) photons associated with ValueMaps
process.prefiringweight = cms.EDProducer("L1ECALPrefiringWeightProducer",
        ThePhotons = cms.InputTag("slimmedPhotons",processName=cms.InputTag.skipCurrentProcess()),
        TheJets = cms.InputTag("slimmedJets"),
        L1Maps = cms.string(cmssw_base+"/src/BaconProd/Utils/data/L1PrefiringMaps_new.root"),
        DataEra = cms.string("2016BtoH"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUncty = cms.double(0.2)
        )

#--------------------------------------------------------------------------------
# Input settings
#================================================================================
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring('/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/270000/4C8E5D5B-47C7-E811-826C-0CC47A0AD48A.root')
        )

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
        outputName          = cms.untracked.string('Trimmed_MC.root'),
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
                minPt                     = cms.untracked.double(5),
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
                minPt                     = cms.untracked.double(3),
                edmName                   = cms.untracked.string('slimmedMuons'),
                edmPuppiName              = cms.untracked.string('puppi'),
                edmPuppiNoLepName         = cms.untracked.string('puppiNoLep'),
                usePuppi                  = cms.untracked.bool(False),    
                fillVertices              = cms.untracked.bool(False),
                useTriggerObject          = cms.untracked.bool(True),
                ),
        )

process.baconSequence = cms.Sequence(
        process.egammaPostRecoSeq                  *
        process.prefiringweight                    *
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
