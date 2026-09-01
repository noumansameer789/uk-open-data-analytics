# Reproducible analytics on UK open government data

Production-style data-quality and reporting components from three linked
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
