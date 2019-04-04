#!/bin/sh

echo "Job submitted on host `hostname` on `date`"
echo ">>> arguments: $@"

### Required parameters #####
CONFIGFILE=$1
EOSPATH=$2
JOBID=$3
INFILE=$4

### Transfer files, prepare directory ###
export SCRAM_ARCH=slc6_amd64_gcc630
export CMSSW_VERSION=CMSSW_9_4_12
source /cvmfs/cms.cern.ch/cmsset_default.sh

tar -xzf source.tar.gz
cd $CMSSW_VERSION/src/
scramv1 b ProjectRename
cmsenv
cd BaconProd/Ntupler/config

echo $CONFIG
pwd

### Run the analyzer
cmsRun $CONFIGFILE maxEvents=-1 inputFiles=$INFILE

### Copy output and cleanup ###
if xrdcp -s Output.root root://cmseos.fnal.gov/${EOSPATH}/Output_${JOBID}.root
then
    echo "Copied output to root://cmseos.fnal.gov/${EOSPATH}/Output_${JOBID}.root"
fi
rm Output.root
