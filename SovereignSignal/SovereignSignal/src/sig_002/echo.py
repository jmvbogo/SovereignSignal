def detect_delta(verdicts):
    scores = [v['score'] for v in verdicts]
    delta = max(scores) - min(scores)
    return delta