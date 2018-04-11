#include "BaconProd/Ntupler/interface/FillerVertex.hh"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "BaconAna/DataFormats/interface/TVertex.hh"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include <TClonesArray.h>

using namespace baconhep;

//--------------------------------------------------------------------------------------------------
FillerVertex::FillerVertex(const edm::ParameterSet &iConfig, const bool useAOD, edm::ConsumesCollector && iC):
  fPVName       (iConfig.getUntrackedParameter<std::string>("edmName","offlinePrimaryVertices")),
  fMinNTracksFit(0),
  fMinNdof      (4),
  fMaxAbsZ      (24),
  fMaxRho       (2),
  fUseAOD       (useAOD)
{
  fTokVertex       = iC.consumes<reco::VertexCollection>(fPVName); 
}

//--------------------------------------------------------------------------------------------------
FillerVertex::~FillerVertex(){}

//--------------------------------------------------------------------------------------------------
const reco::Vertex* FillerVertex::fill(TClonesArray *array, int &nvtx, const edm::Event &iEvent)
{
  assert(array);
  
  // Get vertex collection
  edm::Handle<reco::VertexCollection> hVertexProduct;
  iEvent.getByToken(fTokVertex,hVertexProduct);
  assert(hVertexProduct.isValid());
  const reco::VertexCollection *pvCol = hVertexProduct.product();

  const reco::Vertex* pv = &(*pvCol->begin());
  nvtx = 0;
    
  for(reco::VertexCollection::const_iterator itVtx = pvCol->begin(); itVtx!=pvCol->end(); ++itVtx) { 
    //std::cout << "processing new vertex" << std::endl;
    if(fUseAOD) {
      if(itVtx->isFake())                        continue;
    } else {
      if(itVtx->chi2()==0 && itVtx->ndof()==0)   continue;  //(!) substitute for Vertex::isFake() because track collection not in MINIAOD
    }
    if(itVtx->tracksSize()     < fMinNTracksFit) {
        //std::cout << "cut vertex at " << itVtx->x() << ", " << itVtx->y() << ", " << itVtx->z() << std::endl;
        continue;
    }
    //std::cout << "passed track size cut" << std::endl;
    if(itVtx->ndof()           < fMinNdof) {
        //std::cout << "cut vertex at " << itVtx->x() << ", " << itVtx->y() << ", " << itVtx->z() << std::endl;
        //std::cout << "cut ndof value was " << itVtx->ndof() << std::endl;
        continue;
    }
    //std::cout << "passed ndof cut" << std::endl;
    if(fabs(itVtx->z())        > fMaxAbsZ) {
        //std::cout << "cut vertex at " << itVtx->x() << ", " << itVtx->y() << ", " << itVtx->z() << std::endl;
        continue;
    }
    //std::cout << "passed z cut" << std::endl;
    if(itVtx->position().Rho() > fMaxRho) {
        //std::cout << "cut vertex at " << itVtx->x() << ", " << itVtx->y() << ", " << itVtx->z() << std::endl;
        continue;
    }
    //std::cout << "passed rho cut" << std::endl;
    //std::cout << "passed vertex at " << itVtx->x() << ", " << itVtx->y() << ", " << itVtx->z() << std::endl;

    // vertices are sorted by sum{pT^2}, so the first one passing cuts
    // is taken as the event primary vertex
    if(nvtx==0) {
      //std::cout << "THIS VERTEX IS THE CHOSEN ONE" << std::endl;
      pv = &(*itVtx);
    }
    nvtx++;

    // construct object and place in array
    TClonesArray &rArray = *array;
    assert(rArray.GetEntries() < rArray.GetSize());
    const int index = rArray.GetEntries();
    new(rArray[index]) TVertex();
    TVertex *pVertex = (TVertex*)rArray[index];
    
    pVertex->nTracksFit = itVtx->tracksSize();
    pVertex->ndof       = itVtx->ndof();
    pVertex->chi2       = itVtx->chi2();
    pVertex->x          = itVtx->x();
    pVertex->y          = itVtx->y();
    pVertex->z          = itVtx->z();
    pVertex->xerr       = itVtx->xError();
    pVertex->yerr       = itVtx->yError();
    pVertex->zerr       = itVtx->zError();
  }
  return pv;
}
