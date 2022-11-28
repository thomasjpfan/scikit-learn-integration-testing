# Scikit-learn Integration Testing

[![Build Status](https://dev.azure.com/thomasjpfan/scikit-learn/_apis/build/status/thomasjpfan.scikit-learn-integration-testing?branchName=main)](https://dev.azure.com/thomasjpfan/scikit-learn/_build/latest?definitionId=10&branchName=main)

This repository tests the compatibility of scikit-learn with specific downstream libraries by using [TexasBBQ](https://github.com/numba/texasbbq).

## Tested Projects

- [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)

## Adding a New Downstream Library

- Implement the logic for the target, by subclassing `texasbbq.CondaTarget` or
`texasbbq.GitTarget` in the `switchboard.py`. Refer to [TexasBBQ](https://github.com/numba/texasbbq) for details.
- Add an a new target in `azure-pipelines.yml` under `matrix`.
- Update the `README.md` to reflect the current list of projets being tested.
- Add library name to `.gitignore` to ignore folder when testing locally.
- Submit a PR to Github.

## License

MIT
