#!/usr/bin/env python3

from pathlib import Path
import argparse

import numpy as np
import robustocs as rocs


ROOT = Path("/opt/robustocs-upstream")


def run_example() -> int:
    sigma, mubar, omega, n, _, _, _ = rocs.load_problem(
        sigma_filename=str(ROOT / "examples" / "04" / "A04.txt"),
        mu_filename=str(ROOT / "examples" / "04" / "EBV04.txt"),
        omega_filename=str(ROOT / "examples" / "04" / "S04.txt"),
        sex_filename=str(ROOT / "examples" / "04" / "SEX04.txt"),
        issparse=True,
    )
    sires = range(0, n, 2)
    dams = range(1, n, 2)
    lam = 0.5
    kap = 1
    true_std = np.array([0, 0, 0.5, 0.5])
    true_rob = np.array([0.382, 0.382, 0.118, 0.118])
    w_std, _ = rocs.highs_standard_genetics(sigma, mubar, sires, dams, lam, n)
    w_rob, z_rob, _ = rocs.highs_robust_genetics(
        sigma, mubar, omega, sires, dams, lam, kap, n
    )
    if not np.allclose(w_std, true_std, atol=1e-7):
        raise SystemExit("standard HiGHS result did not match the expected example")
    if not np.allclose(w_rob, true_rob, atol=1e-3):
        raise SystemExit("robust HiGHS result did not match the expected example")
    if not rocs.check_uncertainty_constraint(z_rob, w_rob, omega, debug=False):
        raise SystemExit("uncertainty constraint check failed")
    print("Success")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="robustocs",
        description="Picotainers wrapper for the RobustOCS Python package",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=rocs.__version__,
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("example", help="run the bundled HiGHS smoke test")
    args = parser.parse_args(argv)
    if args.command == "example":
        return run_example()
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
