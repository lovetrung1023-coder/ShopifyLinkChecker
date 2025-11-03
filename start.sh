#!/usr/bin/env bash
set -euo pipefail

# Set timezone to US West (Oregon) - Pacific Time
export TZ=America/Los_Angeles

# Verify timezone setting
echo "Current timezone: $TZ"
date

# Install dependencies (Render will already run buildCommand but keep here for shell runs)
pip install -r requirements.txt

# Run migrations (safe if tables already exist)
python migrate_to_db.py || echo "Migration script exited with non-zero code (continuing)"

# Start Streamlit (bind to Render port)
exec streamlit run app.py --server.port $PORT --server.address 0.0.0.0
