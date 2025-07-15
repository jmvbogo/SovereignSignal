"""
Data models for Sovereign Signal.
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Claim:
    claim_id: str
    text: str
    source_id: str
    timestamp: str

@dataclass
class Verdict:
    claim_id: str
    node_id: str
    score: float
    timestamp: str
    details: dict
