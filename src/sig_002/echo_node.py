"""
SIG-002: Echo Node - Monitors Aletheia nodes for consensus and computes Delta.
"""
import logging

logger = logging.getLogger(__name__)

class EchoNode:
    """
    Echo Node listens to verdicts and computes volatility (Delta).
    """
    def __init__(self, node_id: str):
        self.node_id = node_id
        logger.info(f"Echo Node {self.node_id} initialized.")

    def compute_delta(self, verdicts: list) -> float:
        """
        Calculates the delta as max(score)-min(score) among verdicts.
        """
        scores = [v.score for v in verdicts]
        delta = max(scores) - min(scores) if scores else 0.0
        logger.debug(f"Computed delta: {delta}")
        return delta
