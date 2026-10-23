"""Fail if any .json file in the repository is not valid JSON."""
import json
import pathlib
import sys

bad = 0
for p in pathlib.Path(".").rglob("*.json"):
    if ".git" in p.parts:
        continue
    try:
        json.loads(p.read_text())
    except ValueError as e:
        bad += 1
        print(f"INVALID {p}: {e}")
print("json files checked; invalid:", bad)
sys.exit(1 if bad else 0)
