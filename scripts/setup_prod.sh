#!/bin/bash

if test -z $CMSSW_VERSION; then
    echo "[BaconProd] Need CMSSW project area setup!";
    echo
    return 0;
fi

CURRDIR=$PWD
cd $CMSSW_BASE/src

git cms-init
git cms-merge-topic cms-egamma:EgammaID_949
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940
git cms-merge-topic lathomas:L1Prefiring_9_4_9

echo
echo "[BaconProd] Setup complete!"

cd $CURRDIR

return 1;
