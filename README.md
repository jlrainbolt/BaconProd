BaconProd
=========

Package for producing bacon ntuples

 * Run on CMS LPC
 * CMSSW_8_0_26_patch1
 * Depends on NWUHEP/BaconAna topic_jbueghly branch

Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_8_0_26_patch1
cd CMSSW_8_0_26_patch1
cmsenv
git cms-init
git cms-merge-topic rafaellopesdesa:RegressionCheckNegEnergy
git cms-merge-topic cms-egamma:EGM_gain_v1
cd EgammaAnalysis/ElectronTools/data/
git clone -b Moriond17_gainSwitch_unc https://github.com/ECALELFS/ScalesSmearings.git
cd $CMSSW_BASE/src
```

* edit EgammaAnalysis/ElectronTools/python/calibrationTablesRun2.py
    + change correctionType to "Moriond17_23Jan"

```Shell
git cms-merge-topic cms-met:METRecipe_8020 -u 
git cms-merge-topic cms-met:METRecipe_80X_part2 -u
git cms-merge-topic ikrav:egm_id_80X_v3_photons
git clone -b topic_jbueghly git@github.com:NWUHEP/BaconAna
git clone -b topic_jbueghly git@github.com:NWUHEP/BaconProd
cp -r /uscms/home/jbueghly/nobackup/bacon/xmas_bacon_2017/CMSSW_8_0_26_patch1/src/ShowerDeconstruction/ .
cp -r /uscms/home/jbueghly/nobackup/bacon/xmas_bacon_2017/CMSSW_8_0_26_patch1/src/RecoMET/METPUSubtraction/ RecoMET/
cp -r /uscms/home/jbueghly/nobackup/bacon/xmas_bacon_2017/CMSSW_8_0_26_patch1/src/PhysicsTools .
scram b clean
scram b -j 12
```

* to run, navigate to BaconProd/Ntupler/config
    + Data: cmsRun makingBacon_Data_25ns_MINIAOD.py
    + MC: cmsRun makingBacon_MC_25ns_MINIAOD.py



