# Reproducible analytics on UK open government data

> **Provenance and scope.** MTHM503 MSc coursework, June 2026. This portfolio reconstruction contains selected data-quality and statistical diagnostics with tests. The assessed Quarto analyses, PostgreSQL environment and full source extracts are not reproduced here. Headline results and the original 25-test count describe the coursework, not this smaller repository.

Selected data-quality and reporting components from three linked
analyses of Energy Performance Certificate and STATS19 data.

## Reported result from the original experiment

- 66,987 EPC records; LDA achieved 0.74 accuracy and 0.74 macro-F1 on 20,097
  held-out rows, versus 0.62 for QDA
- mixed-effects analysis used 6,917 observations across 346 local authorities
- the original pipeline passed 25 tests and used `doit`, Quarto, flake8 and
  GitHub Actions

## Judgement preserved

A near-zero random-effect variance produced a singular fit. The project treated
fixed effects as interpretable but rejected an authority ranking. The executable
diagnostic returns that warning rather than allowing a misleading league table.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Private PostgreSQL credentials, assessment material and server extracts are not
published. `file_sha256` supports a reproducible manifest when public extracts
are added.


## Licence

Original material is available for portfolio evaluation under the [evaluation-only licence](LICENSE). Third-party data, libraries and original assessment materials retain their own terms.
