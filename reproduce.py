"""Reproduce the supplied synthetic analyses from the repository root."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
COMMANDS = ['code/provenance_contract.py', 'code/check_R2_reduction.py', 'code/exact_certificate.py', 'code/reproduce.py']
for script in COMMANDS:
    print(f"Running {script}", flush=True)
    subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, check=True)
print("All selected scientific reproduction scripts completed successfully.")
