# Sovereign Signal v1.0 Alpha: Operational Guide

## Introduction
The Sovereign Signal v1.0 Alpha is a decentralized, verifiable truth-discernment system. It processes claims, reaches consensus, and records every step into immutable logs.

## Architecture
- **SIG-001 (Aletheia Node):** Independent analysis of claims.
- **SIG-002 (Echo Node):** Monitors verdicts and computes Delta.
- **Consensus Engine:** Calculates quorum and determines action paths.
- **Web UI (Veracity Chronicle):** Public dashboard and watch queue.
- **Tasks:** Scheduled exports, blockchain notarization, uptime monitoring.
- **Audit Logs:** Immutable append-only records in `output/`.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/jmvbogo/SovereignSignal.git
   cd SovereignSignal
   ```
2. Setup environment (see `scripts/setup_env.sh`).

## Configuration
Populate `.env` based on `.env.template`. Review `config/*.json` for consensus, webhook, and notarization settings.

## Usage
- Start services: `scripts/run_all.sh`
- Submit claims via API: `POST /api/submit_claim`

