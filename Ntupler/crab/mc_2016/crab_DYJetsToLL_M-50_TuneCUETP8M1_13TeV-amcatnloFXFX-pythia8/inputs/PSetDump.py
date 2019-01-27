import FWCore.ParameterSet.Config as cms

process = cms.Process("MakingBacon")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(''),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_MEtoEDMConverter_*_*')
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497),
    HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209),
    HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593),
    HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06)
)

process.maxEvents = cms.untracked.PSet(
    output = cms.untracked.int32(5000)
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Phys14NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.253', 
            ' 0.081', 
            '-0.081', 
            ' 0.965', 
            ' 0.917', 
            ' 0.683'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.483', 
            '-0.267', 
            '-0.323', 
            ' 0.933', 
            ' 0.825', 
            ' 0.337'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_Trig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15Trig25nsV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vstring('0.988153', 
            '0.96791', 
            '0.841729'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vstring('0.972153', 
            '0.922126', 
            '0.610764'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring(' 0.287435', 
            ' 0.221846', 
            '-0.303263', 
            ' 0.967083', 
            ' 0.929117', 
            ' 0.726311'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring('-0.083313', 
            '-0.235222', 
            '-0.67099', 
            ' 0.913286', 
            ' 0.805013', 
            ' 0.358969'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vstring(' -0.265', 
            ' -0.556', 
            ' -0.551', 
            ' -0.072', 
            ' -0.286', 
            ' -0.267'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring15Trig50nsV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vstring('0.981841', 
            '0.946762', 
            '0.79704'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vstring('0.953843', 
            '0.849994', 
            '0.514118'),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
)

process.mvaPhoID_RunIIFall17_v1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v1p1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v2'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
)

process.mvaPhoID_RunIIFall17_v2_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(0.42, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(-0.02, -0.26),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring16NonTrigV1'),
    nCategories = cms.int32(2),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    fileMode = cms.untracked.string('NOMERGE'),
    wantSummary = cms.untracked.bool(False)
)

process.trkIsol03CfgV2 = cms.PSet(
    barrelCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.1),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    ),
    endcapCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.5),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Phys14NonTrig25nsV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15NonTrig25nsV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15Trig50nsV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring15Trig25nsV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
    ))

process.mvaConfigsForPhoProducer = cms.VPSet(cms.PSet(
    categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring16NonTrigV1'),
        nCategories = cms.int32(2),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
    ), 
    cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v2'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
    ))

process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(35.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.4442),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.566)
                        )),
                    cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDEtaInSeedCut'),
                    dEtaInSeedCutValueEB = cms.double(0.004),
                    dEtaInSeedCutValueEE = cms.double(0.006),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDPhiInCut'),
                    dPhiInCutValueEB = cms.double(0.06),
                    dPhiInCutValueEE = cms.double(0.06),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaWithSatCut'),
                    isIgnored = cms.bool(False),
                    maxNrSatCrysIn5x5EB = cms.int32(0),
                    maxNrSatCrysIn5x5EE = cms.int32(0),
                    maxSigmaIEtaIEtaEB = cms.double(9999),
                    maxSigmaIEtaIEtaEE = cms.double(0.03),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    cutName = cms.string('GsfEleFull5x5E2x5OverE5x5WithSatCut'),
                    isIgnored = cms.bool(False),
                    maxNrSatCrysIn5x5EB = cms.int32(0),
                    maxNrSatCrysIn5x5EE = cms.int32(0),
                    minE1x5OverE5x5EB = cms.double(0.83),
                    minE1x5OverE5x5EE = cms.double(-1.0),
                    minE2x5OverE5x5EB = cms.double(0.94),
                    minE2x5OverE5x5EE = cms.double(-1.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    constTermEB = cms.double(1.0),
                    constTermEE = cms.double(5),
                    cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    slopeStartEB = cms.double(0.0),
                    slopeStartEE = cms.double(0.0),
                    slopeTermEB = cms.double(0.05),
                    slopeTermEE = cms.double(0.05)
                ), 
                cms.PSet(
                    constTermEB = cms.double(5.0),
                    constTermEE = cms.double(5.0),
                    cutName = cms.string('GsfEleValueMapIsoRhoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag(""),
                    rhoEAEB = cms.double(0.0),
                    rhoEAEE = cms.double(0.0),
                    rhoEtStartEB = cms.double(999999.0),
                    rhoEtStartEE = cms.double(999999.0),
                    slopeStartEB = cms.double(0.0),
                    slopeStartEE = cms.double(0.0),
                    slopeTermEB = cms.double(0.0),
                    slopeTermEE = cms.double(0.0),
                    value = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
                ), 
                cms.PSet(
                    constTermEB = cms.double(2.0),
                    constTermEE = cms.double(2.5),
                    cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    rhoConstant = cms.double(0.28),
                    slopeStartEB = cms.double(0.0),
                    slopeStartEE = cms.double(50.0),
                    slopeTermEB = cms.double(0.03),
                    slopeTermEE = cms.double(0.03)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDxyCut'),
                    dxyCutValueEB = cms.double(0.02),
                    dxyCutValueEE = cms.double(0.05),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleMissingHitsCut'),
                    isIgnored = cms.bool(False),
                    maxMissingHitsEB = cms.uint32(1),
                    maxMissingHitsEE = cms.uint32(1),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEcalDrivenCut'),
                    ecalDrivenEB = cms.int32(1),
                    ecalDrivenEE = cms.int32(1),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                )),
            idName = cms.string('heepElectronID-HEEPV70'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        idMD5 = cms.string('49b6b60e9f16727f241eb34b9d345a8f'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00387),
                        dEtaInSeedCutValueEE = cms.double(0.0072),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0716),
                        dPhiInCutValueEE = cms.double(0.147),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0414),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.133),
                        isoCutEBLowPt = cms.double(0.133),
                        isoCutEEHighPt = cms.double(0.146),
                        isoCutEELowPt = cms.double(0.146),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('0.9530240956555949 - exp(-pt / 2.7591425841003647) *  0.4669644718545271', 
                        '0.9336564763961019 - exp(-pt /  2.709276284272272) * 0.33512286599215946', 
                        '0.9313133688365339 - exp(-pt / 1.5821934800715558) *  3.8889462619659265', 
                        '0.9825268564943458 - exp(-pt /  8.702601455860762) *  1.1974861596609097', 
                        '0.9727509457929913 - exp(-pt /  8.179525631018565) *  1.7111755094657688', 
                        '0.9562619539540145 - exp(-pt /  8.109845366281608) *   3.013927699126942'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('0.9165112826974601 - exp(-pt / 2.7381703555094217) *    1.03549199648109', 
                        '0.8655738322220173 - exp(-pt / 2.4027944652597073) *  0.7975615613282494', 
                        '-3016.035055227131 - exp(-pt / -52140.61856333602) * -3016.3029387236506', 
                        '0.9616542816132922 - exp(-pt /  8.757943837889817) *  3.1390200321591206', 
                        '0.9319258011430132 - exp(-pt /  8.846057432565809) *  3.5985063793347787', 
                        '0.8899260780999244 - exp(-pt / 10.124234115859881) *   4.352791250718547'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring('-0.13285867293779202', 
                        '-0.31765300958836074', 
                        '-0.0799205914718861', 
                        '-0.856871961305474', 
                        '-0.8107642141584835', 
                        '-0.7179265933023059'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring('0.9725509559754997 - exp(-pt /  2.976593261509491) *  0.2653858736397496', 
                        '0.9508038141601247 - exp(-pt / 2.6633500558725713) *  0.2355820499260076', 
                        '0.9365037167596238 - exp(-pt / 1.5765442323949856) *   3.067015289215309', 
                        '0.9896562087723659 - exp(-pt / 10.342490511998674) * 0.40204156417414094', 
                        '0.9819232656533827 - exp(-pt /   9.05548836482051) *   0.772674931169389', 
                        '0.9625098201744635 - exp(-pt /   8.42589315557279) *  2.2916152615134173'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring('0.9387070396095831 - exp(-pt /   2.6525585228167636) *  0.8222647164151365', 
                        '0.8948802925677235 - exp(-pt /   2.7645670358783523) *  0.4123381218697539', 
                        '-1830.8583661119892 - exp(-pt /   -36578.11055382301) * -1831.2083578116517', 
                        '0.9717674837607253 - exp(-pt /    8.912850985100356) *  1.9712414940437244', 
                        '0.9458745023265976 - exp(-pt /     8.83104420392795) *    2.40849932040698', 
                        '0.8979112012086751 - exp(-pt /    9.814082144168015) *   4.171581694893849'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring('-0.09564086146419018', 
                        '-0.28229916981926795', 
                        '-0.05466682296962322', 
                        '-0.833466688584422', 
                        '-0.7677000247570116', 
                        '-0.6917305995653829'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring('0.940962684155', 
                        '0.899208843708', 
                        '0.758484721184'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring('0.836695742607', 
                        '0.715337944031', 
                        '0.356799721718'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    mvaCuts = cms.vstring('-0.211', 
                        '-0.396', 
                        '-0.215', 
                        '-0.870', 
                        '-0.838', 
                        '-0.763'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-HZZ-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1797cc03eb62387e10266fca72ea10cd'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00377),
                        dEtaInSeedCutValueEE = cms.double(0.00674),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0884),
                        dPhiInCutValueEE = cms.double(0.169),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0112),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0425),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0441),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.111),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.112),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.108),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('5547e2c8b5c222192519c41bff05bc2e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.0032),
                        dEtaInSeedCutValueEE = cms.double(0.00632),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0547),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0106),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0387),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.046),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0275),
                        endcapCE = cms.double(2.52),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.184),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0721),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0478),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0658),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('48702f025a8df2c527f53927af8b66d0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00255),
                        dEtaInSeedCutValueEE = cms.double(0.00501),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.022),
                        dPhiInCutValueEE = cms.double(0.0236),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0353),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.15),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0188),
                        endcapCE = cms.double(2.06),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.159),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0197),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0287),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0445),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c06761e199f084f5b0f7868ac48a3e19'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00463),
                        dEtaInSeedCutValueEE = cms.double(0.00814),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.148),
                        dPhiInCutValueEE = cms.double(0.19),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0126),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0457),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.209),
                        eInverseMinusPInverseCutValueEE = cms.double(0.132),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.198),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.203),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('74e217e3ece16b49bd337026a29fc3e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring('3.26449620468 - exp(-pt / 3.32657149223) * 8.84669783568', 
                        '2.83557838497 - exp(-pt / 2.15150487651) * 11.0978016567', 
                        '2.91994945177 - exp(-pt / 1.69875477522) * 24.024807824', 
                        '7.1336238874 - exp(-pt / 16.5605268797) * 8.22531222391', 
                        '6.18638275782 - exp(-pt / 15.2694634284) * 7.49764565324', 
                        '5.43175865738 - exp(-pt / 15.4290075949) * 7.56899692285'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring('2.77072387339 - exp(-pt / 3.81500912145) * 8.16304860178', 
                        '1.85602317813 - exp(-pt / 2.18697654938) * 11.8568936824', 
                        '1.73489307814 - exp(-pt / 2.0163211971) * 17.013880078', 
                        '5.9175992258 - exp(-pt / 13.4807294538) * 9.31966232685', 
                        '5.01598837255 - exp(-pt / 13.1280451502) * 8.79418193765', 
                        '4.16921343208 - exp(-pt / 13.2017224621) * 9.00720913211'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring('0.894411158628', 
                        '0.791966464633', 
                        '1.47104857173', 
                        '-0.293962958665', 
                        '-0.250424758584', 
                        '-0.130985179031'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring('3.53495358797 - exp(-pt / 3.07272325141) * 9.94262764352', 
                        '3.06015605623 - exp(-pt / 1.95572234114) * 14.3091184421', 
                        '3.02052519639 - exp(-pt / 1.59784164742) * 28.719380105', 
                        '7.35752275071 - exp(-pt / 15.87907864) * 7.61288809226', 
                        '6.41811074032 - exp(-pt / 14.730562874) * 6.96387331587', 
                        '5.64936312428 - exp(-pt / 16.3664949747) * 7.19607610311'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring('2.84704783417 - exp(-pt / 3.32529515837) * 9.38050947827', 
                        '2.03833922005 - exp(-pt / 1.93288758682) * 15.364588247', 
                        '1.82704158461 - exp(-pt / 1.89796754399) * 19.1236071158', 
                        '6.12931925263 - exp(-pt / 13.281753835) * 8.71138432196', 
                        '5.26289004857 - exp(-pt / 13.2154971491) * 8.0997882835', 
                        '4.37338792902 - exp(-pt / 14.0776094696) * 8.48513324496'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring('1.26402092475', 
                        '1.17808089508', 
                        '1.33051972806', 
                        '2.36464785939', 
                        '2.07880614597', 
                        '1.08080644615'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpHZZ'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring('0.700642584415', 
                        '0.739335420875', 
                        '1.45390456109', 
                        '-0.146270871164', 
                        '-0.0315850882679', 
                        '-0.0321841194737'),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('PhoSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                    hadronicOverEMCutValueEB = cms.double(0.105),
                    hadronicOverEMCutValueEE = cms.double(0.029),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                    cutValueEB = cms.double(0.0103),
                    cutValueEE = cms.double(0.0276),
                    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(2.839),
                    C1_EE = cms.double(2.15),
                    C2_EB = cms.double(0),
                    C2_EE = cms.double(0.0),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(9.188),
                    C1_EE = cms.double(10.471),
                    C2_EB = cms.double(0.0126),
                    C2_EE = cms.double(0.0119),
                    C3_EB = cms.double(2.6e-05),
                    C3_EE = cms.double(2.5e-05),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(2.956),
                    C1_EE = cms.double(4.895),
                    C2_EB = cms.double(0.0035),
                    C2_EE = cms.double(0.004),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                )),
            idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-loose'),
            isPOGApproved = cms.untracked.bool(True)
        ),
        idMD5 = cms.string('45515ee95e01fa36972ff7ba69186c97'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.035),
                        hadronicOverEMCutValueEE = cms.double(0.027),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.416),
                        C1_EE = cms.double(1.012),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.491),
                        C1_EE = cms.double(9.131),
                        C2_EB = cms.double(0.0126),
                        C2_EE = cms.double(0.0119),
                        C3_EB = cms.double(2.6e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.952),
                        C1_EE = cms.double(4.095),
                        C2_EB = cms.double(0.004),
                        C2_EE = cms.double(0.004),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('772f7921fa146b630e4dbe79e475a421'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02),
                        hadronicOverEMCutValueEE = cms.double(0.025),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.158),
                        C1_EE = cms.double(0.575),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.267),
                        C1_EE = cms.double(8.916),
                        C2_EB = cms.double(0.0126),
                        C2_EE = cms.double(0.0119),
                        C3_EB = cms.double(2.6e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.065),
                        C1_EE = cms.double(3.272),
                        C2_EB = cms.double(0.0035),
                        C2_EE = cms.double(0.004),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('e260fee6f9011fb13ff56d45cccd21c5'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    mvaCuts = cms.vdouble(0.67, 0.54),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('7e48c47329d7d1eb889100ed03a02ba9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    mvaCuts = cms.vdouble(0.27, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('834dd792692b6a62786bd1caa6b53a68'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.67, 0.54),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('56138c4a3ac3c0bffc7f01c187063102'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.27, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1120f91d15f68bf61b5f08958bf4f435'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0481),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01031),
                        cutValueEE = cms.double(0.03013),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.295),
                        C1_EE = cms.double(1.011),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(10.91),
                        C1_EE = cms.double(5.931),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(3.63),
                        C1_EE = cms.double(6.641),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('d6ce6a4f3476294bf0a3261e00170daf'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0396),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01022),
                        cutValueEE = cms.double(0.03001),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.441),
                        C1_EE = cms.double(0.442),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.725),
                        C1_EE = cms.double(1.715),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.571),
                        C1_EE = cms.double(3.863),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c739cfd0b6287b8586da187c06d4053f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0269),
                        hadronicOverEMCutValueEE = cms.double(0.0213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00994),
                        cutValueEE = cms.double(0.03),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.202),
                        C1_EE = cms.double(0.034),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.264),
                        C1_EE = cms.double(0.586),
                        C2_EB = cms.double(0.0148),
                        C2_EE = cms.double(0.0163),
                        C3_EB = cms.double(1.7e-05),
                        C3_EE = cms.double(1.4e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.362),
                        C1_EE = cms.double(2.617),
                        C2_EB = cms.double(0.0047),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('bdb623bdb1a15c13545020a919dd9530'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.68, 0.6),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('beb95233f7d1e033ad9e20cf3d804ba0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.2, 0.2),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('36efe663348f95de0bc1cfa8dc7fa8fe'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(0.42, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('3013ddce7a3ad8b54827c29f5d92282e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(-0.02, -0.26),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('5c06832759b1faf7dd6fc45ed1aef3a2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.04596),
                        hadronicOverEMCutValueEE = cms.double(0.059),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.694),
                        C1_EE = cms.double(2.089),
                        C2_EB = cms.double(0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(24.032),
                        C1_EE = cms.double(19.722),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.876),
                        C1_EE = cms.double(4.162),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4578dfcceb0bfd1ba5ac28973c843fd0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02197),
                        hadronicOverEMCutValueEE = cms.double(0.0326),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01015),
                        cutValueEE = cms.double(0.0272),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.141),
                        C1_EE = cms.double(1.051),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.189),
                        C1_EE = cms.double(2.718),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.08),
                        C1_EE = cms.double(3.867),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('28b186c301061395f394a81266c8d7de'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02148),
                        hadronicOverEMCutValueEE = cms.double(0.0321),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00996),
                        cutValueEE = cms.double(0.0271),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.65),
                        C1_EE = cms.double(0.517),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.317),
                        C1_EE = cms.double(2.716),
                        C2_EB = cms.double(0.01512),
                        C2_EE = cms.double(0.0117),
                        C3_EB = cms.double(2.259e-05),
                        C3_EE = cms.double(2.3e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(2.044),
                        C1_EE = cms.double(3.032),
                        C2_EB = cms.double(0.004017),
                        C2_EE = cms.double(0.0037),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('6f4f0ed6a8bf2de8dcf0bc3349b0546d'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h+'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
        vertexIndex = cms.int32(0)
    ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        )),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Phys14NonTrig25nsV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2VariablesClassic.txt'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15NonTrig25nsV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15Trig50nsV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring15Trig25nsV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronMVAVariableHelper = cms.EDProducer("GsfElectronMVAVariableHelper",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    beamSpotMiniAOD = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices"),
    vertexCollectionMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.heepIDVarValueMaps = cms.EDProducer("ElectronHEEPIDValueMapProducer",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    candVetosAOD = cms.vstring('ELES', 
        'NONE', 
        'NONELES'),
    candVetosMiniAOD = cms.vstring('ELES', 
        'NONE', 
        'NONELES'),
    candsAOD = cms.VInputTag("packedCandsForTkIso", "lostTracksForTkIso", "lostTracksForTkIso:eleTracks"),
    candsMiniAOD = cms.VInputTag("packedPFCandidates", "lostTracks", "lostTracks:eleTracks"),
    dataFormat = cms.int32(2),
    ebRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    ebRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    eeRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    elesAOD = cms.InputTag("gedGsfElectrons"),
    elesMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    trkIsoConfig = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    )
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring15NonTrig50nsV2p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring15/50ns_EE_V2.weights.xml.gz')
    ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring15NonTrig25nsV2p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring15.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring15/25ns_EE_V2.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring16NonTrigV1'),
            nCategories = cms.int32(2),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz')
        ), 
        cms.PSet(
            categoryCuts = cms.vstring('abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v2'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz')
        )),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonRegressionValueMapProducer = cms.EDProducer("PhotonRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.prefiringweight = cms.EDProducer("L1ECALPrefiringWeightProducer",
    DataEra = cms.string('2016BtoH'),
    L1Maps = cms.string('src/BaconProd/Utils/data/L1PrefiringMaps_new.root'),
    PrefiringRateSystematicUncty = cms.double(0.2),
    TheJets = cms.InputTag("slimmedJets"),
    ThePhotons = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    UseJetEMPt = cms.bool(False)
)


process.slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            electron_config = cms.PSet(
                ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                ElectronMVAEstimatorRun2Spring15Trig25nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
                ElectronMVAEstimatorRun2Spring15Trig50nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
                ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                heepTrkPtIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
            ),
            modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
            overrideExistingValues = cms.bool(True),
            photon_config = cms.PSet(
                PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
                PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
                PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                PhotonMVAEstimatorRunIIFall17v1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
                photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
            )
        ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
                    PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1-wp80"),
                    mvaPhoID_RunIIFall17_v1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1-wp90"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
                ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
                modifierName = cms.string('EG8XObjectUpdateModifier'),
                overrideExistingValues = cms.bool(True)
            ))
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.slimmedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            electron_config = cms.PSet(
                ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                ElectronMVAEstimatorRun2Spring15Trig25nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
                ElectronMVAEstimatorRun2Spring15Trig50nsV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
                ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                heepTrkPtIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso")
            ),
            modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
            overrideExistingValues = cms.bool(True),
            photon_config = cms.PSet(
                PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
                PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
                PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                PhotonMVAEstimatorRunIIFall17v1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Values"),
                PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                phoNeutralHadronIsolation = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
                photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
            )
        ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
                    PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1-wp80"),
                    mvaPhoID_RunIIFall17_v1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1-wp90"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
                )
            ), 
            cms.PSet(
                ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
                ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
                modifierName = cms.string('EG8XObjectUpdateModifier'),
                overrideExistingValues = cms.bool(True)
            ))
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.ntupler = cms.EDAnalyzer("NtuplerMod",
    Electron = cms.untracked.PSet(
        edmEcalPFClusterIsoMapTag = cms.untracked.InputTag("electronEcalPFClusterIsolationProducer"),
        edmHcalPFClusterIsoMapTag = cms.untracked.InputTag("electronHcalPFClusterIsolationProducer"),
        edmName = cms.untracked.string('slimmedElectrons'),
        edmPuppiName = cms.untracked.string('puppi'),
        edmPuppiNoLepName = cms.untracked.string('puppiNoLep'),
        edmSCName = cms.untracked.InputTag("reducedEgamma","reducedSuperClusters"),
        fillVertices = cms.untracked.bool(False),
        isActive = cms.untracked.bool(True),
        minPt = cms.untracked.double(5),
        usePuppi = cms.untracked.bool(False),
        useTriggerObject = cms.untracked.bool(True)
    ),
    GenInfo = cms.untracked.PSet(
        edmGenEventInfoName = cms.untracked.string('generator'),
        edmGenPackParticlesName = cms.untracked.string('packedGenParticles'),
        edmGenParticlesName = cms.untracked.string('prunedGenParticles'),
        fillAllGen = cms.untracked.bool(True),
        fillLHEWeights = cms.untracked.bool(True),
        isActive = cms.untracked.bool(True)
    ),
    Info = cms.untracked.PSet(
        doFillMET = cms.untracked.bool(False),
        doFillMETFilters = cms.untracked.bool(False),
        ecalWeightDownName = cms.untracked.InputTag("prefiringweight","NonPrefiringProbDown"),
        ecalWeightName = cms.untracked.InputTag("prefiringweight","NonPrefiringProb"),
        ecalWeightUpName = cms.untracked.InputTag("prefiringweight","NonPrefiringProbUp"),
        edmBeamspotName = cms.untracked.string('offlineBeamSpot'),
        edmMETName = cms.untracked.string('slimmedMETs'),
        edmMVAMETName = cms.untracked.string(''),
        edmPFCandName = cms.untracked.string('packedPFCandidates'),
        edmPFMETName = cms.untracked.InputTag("slimmedMETsV2","","MakingBacon"),
        edmPileupInfoName = cms.untracked.string('slimmedAddPileupInfo'),
        edmPuppETName = cms.untracked.InputTag("slimmedMETsPuppi","","MakingBacon"),
        edmRhoForIsoName = cms.untracked.string('fixedGridRhoFastjetAll'),
        edmRhoForJetEnergy = cms.untracked.string('fixedGridRhoFastjetAll'),
        isActive = cms.untracked.bool(True)
    ),
    Muon = cms.untracked.PSet(
        edmName = cms.untracked.string('slimmedMuons'),
        edmPuppiName = cms.untracked.string('puppi'),
        edmPuppiNoLepName = cms.untracked.string('puppiNoLep'),
        fillVertices = cms.untracked.bool(False),
        isActive = cms.untracked.bool(True),
        minPt = cms.untracked.double(3),
        usePuppi = cms.untracked.bool(False),
        useTriggerObject = cms.untracked.bool(True)
    ),
    PV = cms.untracked.PSet(
        edmName = cms.untracked.string('offlineSlimmedPrimaryVertices'),
        isActive = cms.untracked.bool(True),
        maxAbsZ = cms.untracked.double(24),
        maxRho = cms.untracked.double(2),
        minNTracksFit = cms.untracked.uint32(0),
        minNdof = cms.untracked.double(4)
    ),
    TriggerFile = cms.untracked.string('BaconAna/DataFormats/data/HLTFile_25ns'),
    TriggerObject = cms.untracked.string('slimmedPatTrigger'),
    edmGenRunInfoName = cms.untracked.string('generator'),
    edmPVName = cms.untracked.string('offlineSlimmedPrimaryVertices'),
    outputName = cms.untracked.string('Output.root'),
    skipOnHLTFail = cms.untracked.bool(False),
    useAOD = cms.untracked.bool(False),
    useTrigger = cms.untracked.bool(True)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(10)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('94X_mcRun2_asymptotic_v3'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497),
        HFdepthOneParameterB = cms.vdouble(-4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209),
        HFdepthTwoParameterA = cms.vdouble(0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593),
        HFdepthTwoParameterB = cms.vdouble(-2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06)
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(cms.PSet(
        crosstalk = cms.double(0.0),
        nonlin1 = cms.double(1.0),
        nonlin2 = cms.double(0.0),
        nonlin3 = cms.double(0.0),
        pixels = cms.int32(36000)
    ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.000439367311072),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(203),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(44.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(203)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.000439367311072),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(203),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(44.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.69e-11, 7.9e-11),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(203)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.egmPhotonIsolationMiniAODTask = cms.Task(process.egmPhotonIsolation)


process.egammaPostRecoPatUpdatorTask = cms.Task(process.slimmedElectrons, process.slimmedPhotons)


process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer, process.electronMVAVariableHelper, process.electronRegressionValueMapProducer)


process.egammaScaleSmearTask = cms.Task()


process.egmPhotonIDTask = cms.Task(process.egmPhotonIDs, process.egmPhotonIsolationMiniAODTask, process.photonIDValueMapProducer, process.photonMVAValueMapProducer, process.photonRegressionValueMapProducer)


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolationMiniAODTask)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIDTask)


process.egammaScaleSmearSeq = cms.Sequence(process.egammaScaleSmearTask)


process.egammaPostRecoPatUpdatorSeq = cms.Sequence(process.egammaPostRecoPatUpdatorTask)


process.egmGsfElectronIDSequence = cms.Sequence(cms.Task(process.heepIDVarValueMaps), process.egmGsfElectronIDTask)


process.egammaPostRecoSeq = cms.Sequence(process.egmGsfElectronIDSequence+process.egammaPostRecoPatUpdatorSeq+process.egmPhotonIDSequence)


process.baconSequence = cms.Sequence(process.egammaPostRecoSeq+process.prefiringweight+process.ntupler)


process.p = cms.EndPath(process.baconSequence)


