#ifndef BACONPROD_NTUPLER_FILLERELECTRON_HH
#define BACONPROD_NTUPLER_FILLERELECTRON_HH

#include "BaconProd/Utils/interface/TriggerTools.hh"
#include <vector>
#include <string>

// forward class declarations
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

class TClonesArray;
namespace trigger {
  class TriggerEvent;
}
namespace pat {
  class Electron;
}


namespace baconhep
{
  class FillerElectron
  {
    public:
       FillerElectron(const edm::ParameterSet &iConfig, const bool useAOD,edm::ConsumesCollector && iC);
      ~FillerElectron();

      // === filler for AOD ===
      void fill(TClonesArray                     *array,                        // output array to be filled
                const edm::Event                 &iEvent,                       // event info
		const edm::EventSetup            &iSetup,                       // event setup info
		const reco::Vertex               &pv,                           // event primary vertex
		const std::vector<TriggerRecord> &triggerRecords,               // list of trigger names and objects
		const trigger::TriggerEvent      &triggerEvent);                // event trigger objects

      // === filler for MINIAOD ===
      void fill(TClonesArray                                 *array,            // output array to be filled
                TClonesArray                                 *array2,            // output array to be filled
                const edm::Event                             &iEvent,           // event info
                const edm::EventSetup                        &iSetup,           // event setup info
                const reco::Vertex                           &pv,               // event primary vertex
                const std::vector<TriggerRecord>             &triggerRecords,   // list of trigger names and objects
                const pat::TriggerObjectStandAloneCollection &triggerObjects);  // event trigger objects

    protected:
    double dEtaInSeed(const reco::GsfElectron& ele);
    double dEtaInSeed(const pat::Electron& ele);      
    void computeIso(double &iEta,double &iPhi, const double extRadius,
		    const reco::PFCandidateCollection    &puppi,
		    float &out_chHadIso, float &out_gammaIso, float &out_neuHadIso) const;    

    void computeIso(double &iEta,double &iPhi, const double extRadius,
		    const pat::PackedCandidateCollection    &puppi,
		    float &out_chHadIso, float &out_gammaIso, float &out_neuHadIso) const;    
  
      // Electron cuts
      double fMinPt;
      
      // EDM object collection names
      std::string fEleName;
      std::string fBSName;
      std::string fPFCandName;
      std::string fTrackName;
      std::string fConvName;
      edm::InputTag fSCName;
      // Puppi
      std::string fPuppiName; 
      std::string fPuppiNoLepName; 
      bool fUsePuppi;

      // PF cluster isolation info (not in AOD)
      edm::InputTag fEcalPFClusterIsoMapTag;
      edm::InputTag fHcalPFClusterIsoMapTag;
      edm::InputTag fEleMediumIdMapTag;
      edm::InputTag fEleTightIdMapTag;
      bool fUseTO;
      bool fFillVertices;
      bool fUseAOD;

      edm::EDGetTokenT<reco::GsfElectronCollection>  fTokEleName;
      edm::EDGetTokenT<pat::ElectronCollection>      fTokPatEleName;
      edm::EDGetTokenT<reco::BeamSpot>               fTokBSName;
      edm::EDGetTokenT<reco::PFCandidateCollection>  fTokPFCandName;
      edm::EDGetTokenT<reco::PFCandidateCollection>  fTokPuppiName;
      edm::EDGetTokenT<reco::PFCandidateCollection>  fTokPuppiNoLepName;
      edm::EDGetTokenT<pat::PackedCandidateCollection>  fTokPuppiPATName;
      edm::EDGetTokenT<pat::PackedCandidateCollection>  fTokPuppiNoLepPATName;
      edm::EDGetTokenT<reco::TrackCollection>        fTokTrackName;
      edm::EDGetTokenT<reco::ConversionCollection>   fTokConvName;
      edm::EDGetTokenT<reco::SuperClusterCollection> fTokSCName;
      edm::EDGetTokenT<edm::ValueMap<float> > fTokEcalPFClusterIsoMap;
      edm::EDGetTokenT<edm::ValueMap<float> > fTokHcalPFClusterIsoMap;
  };
}
#endif
