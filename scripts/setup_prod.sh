#!/bin/bash

if test -z $CMSSW_VERSION; then
  echo "[BaconProd] Need CMSSW project area setup!";
  echo
  return 0;
fi

CURRDIR=$PWD
PATCHDIR=BaconProd/packages
cd $CMSSW_BASE/src

ls $PATCHDIR/*.tar.gz |xargs -n1 tar -xzvf

echo
echo "[BaconProd] Setup complete!"

cd $CURRDIR

return 1;
