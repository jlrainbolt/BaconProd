BaconProd
=========

Branch for producing bacon ntuples of 2018 MiniAOD data (Periods A-C 17Sep2018 rereco, Period D prompt reco) and MC (Autumn18)

 * Runs on CMS LPC
 * Uses CMSSW_10_2_13
 * Depends on jlrainbolt/BaconAna 2016legacy branch


Recipe for setup and running:

```Shell
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git cms-init
git clone -b 2016legacy git@github.com:jlrainbolt/BaconAna
git clone -b 2018prompt git@github.com:jlrainbolt/BaconProd
git cms-merge-topic cms-egamma:EgammaPostRecoTools
git clone -b ScalesSmearing2018_Dev git@github.com:cms-egamma/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data
git cms-merge-topic cms-egamma:EgammaPostRecoTools_dev
scram b -j 12
```

* to run, navigate to BaconProd/Ntupler/config
    + Data: cmsRun trimmedBacon_Data.py
    + MC: cmsRun trimmedBacon_MC.py


Recipe for submitting to Condor:

```Shell
cd $CMSSW_BASE/..
tar --exclude=.git --exclude=crab --exclude=tmp -czvf source.tar.gz CMSSW_10_2_13
mv source.tar.gz CMSSW_10_2_13/src/BaconProd/Ntupler/config/.
```
