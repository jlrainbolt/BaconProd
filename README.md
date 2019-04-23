BaconProd
=========

Package for producing bacon files of 8 TeV data and MC.  Clone of tags/04 with some added conveniences (dependencies, multicrabs, condor submit files).

 * Runs on CMS LPC
 * Uses CMSSW_5_3_20
 * Depends on BaconAna tags/04 (which I have not modified)


Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc472
cmsrel CMSSW_5_3_20
cd CMSSW_5_3_20/src
cmsenv
git clone -b tags/04 git@github.com:jlrainbolt/BaconAna
git clone -b 04legacy git@github.com:jlrainbolt/BaconProd
source BaconProd/scripts/setup_prod.sh
scram b -j 12
```


* to run, navigate to BaconProd/Ntupler/python
    + Data: cmsRun makingBacon_Data.py
    + MC: cmsRun makingBacon_MC.py


Recipe for submitting to Condor:

```Shell
tar --exclude=.git --exclude=crab --exclude=tmp --exclude=packages -czvf source.tar.gz CMSSW_5_3_20
mv source.tar.gz CMSSW_5_3_20/src/BaconProd/Ntupler/python/.
```
