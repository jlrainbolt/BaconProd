BaconProd
=========

Package for producing bacon files

 * Run on CMS LPC
 * CMSSW_9_4_9_cand2
 * Depends on NWUHEP/BaconAna jbueghly_2017 branch

All objects are declared in BaconAna and filled in BaconProd/Ntupler, see e.g.:

[TJet for Jets](https://github.com/NWUHEP/BaconAna/tree/jbueghly_2017/DataFormats/interface/TJet.hh)

[FillerJet for Jets](https://github.com/NWUHEP/BaconProd/tree/jbueghly_2017/Ntupler/src/FillerJet.cc)

Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_9_4_9_cand2
cd CMSSW_9_4_9_cand2/src
cmsenv
git cms-init
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940
git clone -b jbueghly_2017 git@github.com:NWUHEP/BaconAna
git clone -b jbueghly_2017 git@github.com:NWUHEP/BaconProd
tar -xzvf /uscms/home/jbueghly/nobackup/bacon/bacon_2017_prod/jbueghly_2017/CMSSW_9_4_9_cand2/src/jbueghly_2017_depends.tar.gz .
scram b clean
scram b -j 12
```

* to run, navigate to BaconProd/Ntupler/config
    + Data: cmsRun makingBacon_Data_25ns_MINIAOD.py
    + MC: cmsRun makingBacon_MC_25ns_MINIAOD.py
