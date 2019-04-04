BaconProd
=========

Branch for producing bacon ntuples of 2016 legacy (MiniAODv3) and 2017 (MiniAODv2) data and MC

 * Runs on CMS LPC
 * Uses CMSSW_9_4_12
 * Depends on jlrainbolt/BaconAna 2016legacy branch


Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
cmsrel CMSSW_9_4_12
cd CMSSW_9_4_12/src
cmsenv
git cms-init
git clone -b 2016legacy git@github.com:jlrainbolt/BaconAna
git clone -b 2016legacy git@github.com:jlrainbolt/BaconProd
git cms-merge-topic lathomas:L1Prefiring_9_4_9
git cms-merge-topic cms-egamma:EgammaID_949
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940
scram b -j 12
```

* to run, navigate to BaconProd/Ntupler/config
    + Data: cmsRun trimmedBacon_Data_2016.py
    + MC: cmsRun trimmedBacon_MC_2016.py


Recipe for submitting to Condor:

```Shell
tar --exclude=.git --exclude=crab --exclude=tmp -czvf source.tar.gz CMSSW_9_4_12
mv source.tar.gz CMSSW_9_4_12/src/BaconProd/Ntupler/config/.
```
