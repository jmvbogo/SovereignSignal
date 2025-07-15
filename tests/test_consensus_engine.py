import pytest
from src.core.consensus_engine import ConsensusEngine

def test_calculate_consensus():
    engine = ConsensusEngine(quorum_threshold=0.5)
    assert engine.calculate_consensus([0.2, 0.8]) == 0.5

def test_determine_status():
    thresholds = {"low": 0.1, "moderate": 0.3, "high": 0.6}
    engine = ConsensusEngine(quorum_threshold=0.5)
    assert engine.determine_status(0.05, thresholds) == "low"
    assert engine.determine_status(0.4, thresholds) == "high"
