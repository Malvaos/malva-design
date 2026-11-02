"""Regenerates every screenshot that has a script: python3 tools/screenshots/run_all.py (run from anywhere).
defaults.py first (the first state of each app), then the apps that have every state scripted."""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = ["defaults.py", "calculator.py", "ltask.py"]

for s in SCRIPTS:
    print("==", s, flush=True)
    r = subprocess.run([sys.executable, os.path.join(HERE, s)], cwd=os.path.dirname(os.path.dirname(HERE)))
    if r.returncode:
        sys.exit(r.returncode)
