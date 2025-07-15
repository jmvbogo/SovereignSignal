from src.core.models import Claim
from src.core.crypto import sha256_hash

def analyze_claim(claim):
    score = len(claim.content) % 100 / 100.0
    return {'id': claim.id, 'score': score, 'hash': sha256_hash(claim.content)}