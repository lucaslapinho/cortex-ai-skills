"""Run the 23 targeted completion cases, one fresh process per case, three at a time.

This explicitly invokes the user-requested Astra model and can consume model quota.
It neither grades outputs nor executes the full 253-case catalog.
"""
import concurrent.futures
import argparse
import subprocess
import sys
from pathlib import Path

CASES = {
    "cortex-xql-query-engineer": "XQL-ADV-02 XQL-REG-05 XQL-REG-01 XQL-REG-07",
    "cortex-detection-engineer": "DET-ADR-05 DET-ADR-06",
    "cortex-playbook-engineer": "PB-BAS-03 PB-REG-03",
    "cortex-threat-hunter": "CTH-REG-01 CTH-ADV-03 CTH-ADV-02 CTH-TRB-02 CTH-AMB-03 CTH-ADVRS-05 CTH-REG-04 CTH-AMB-01",
    "cortex-tim-engineer": "TIM-A03 TIM-A04 TIM-R07",
    "cortex-platform-engineer": "PLAT-REG-08",
    "cortex-security-engineer": "SEC-REG-07 SEC-INT-03 SEC-TRB-04",
}


def run_case(job):
    skill, case, output = job
    root = Path(__file__).resolve().parents[1]
    evidence = output / f"{case}.md"
    command = [sys.executable, "-B", str(root / "tools/evaluate.py"), "--skill", skill,
               "--cases", case, "--evidence", str(evidence), "--model", "gpt-6-astra"]
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    print(completed.stdout or completed.stderr, flush=True)
    return completed.returncode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New directory for retained case responses")
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output directory must not already exist; prior evidence is never overwritten")
    output = args.output.resolve()
    jobs = [(skill, case, output) for skill, cases in CASES.items() for case in cases.split()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        codes = list(pool.map(run_case, jobs))
    raise SystemExit(1 if any(codes) else 0)
