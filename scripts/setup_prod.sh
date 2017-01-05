#!/bin/bash

if test -z $CMSSW_VERSION; then
  echo "[BaconProd] Need CMSSW project area setup!";
  echo
  return 0;
fi

CURRDIR=$PWD
PATCHDIR=/afs/cern.ch/work/k/ksung/public/Production/11/CMSSW_8_0_20/src
cd $CMSSW_BASE/src

#declare -a PKGS=("DataFormats" "PhysicsTools" "RecoBTag" "RecoBTau" "RecoMET" "ShowerDeconstruction")
declare -a PKGS=("RecoBTag" "RecoBTau" "ShowerDeconstruction")

for n in "${PKGS[@]}"
do
    echo "Copying ${n} from ${PATCHDIR}"
    cp -r ${PATCHDIR}/${n} .
done

echo
echo "[BaconProd] Setup complete!"

cd $CURRDIR
