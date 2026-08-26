# RobustOCS

Docker container for the [RobustOCS](https://github.com/Foggalong/RobustOCS) Python package.

RobustOCS solves robust optimal contribution selection problems for genetics and supports both Gurobi and HiGHS backends.

Paper citation: Fogg J, Ortiz-Cuadros J, Pocrnic I, Hall JAJ, Gorjanc G. *robustocs: Robust Optimal Contribution Selection*. Bioinformatics. 2026;42(8):btag569. DOI: 10.1093/bioinformatics/btag569.

## Pull

```bash
docker pull picotainers/robustocs:latest
```

## Usage

Show help:

```bash
docker run --rm picotainers/robustocs:latest --help
```

Run the bundled HiGHS smoke example:

```bash
docker run --rm picotainers/robustocs:latest example
```

## Runtime notes

- The image installs `robustocs` into a Python 3.11 virtual environment.
- The bundled smoke example uses the open-source HiGHS backend.
- Gurobi-backed functions are present in the package, but they may still require a valid Gurobi license at runtime.
