BaconProd
=========

Branch for producing bacon ntuples of 2016 legacy data and MC

 * "Runs" on CMS LPC
 * Uses CMSSW_9_4_12
 * Depends on NWUHEP/BaconAna 2016legacy branch


Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_9_4_12
cd CMSSW_9_4_12/src
cmsenv
git cms-init
git clone -b 2016legacy git@github.com:NWUHEP/BaconAna
git clone -b 2016legacy git@github.com:NWUHEP/BaconProd
git cms-merge-topic cms-egamma:EgammaID_949
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940
git cms-merge-topic lathomas:L1Prefiring_9_4_9
scram b -j 12
```

* to run, navigate to BaconProd/Ntupler/config
    + Data: cmsRun makingBacon_Data_25ns_MINIAOD.py
    + MC: cmsRun makingBacon_MC_25ns_MINIAOD.py
