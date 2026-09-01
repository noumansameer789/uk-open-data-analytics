"""Defensive diagnostics used across the UK open-data analytics portfolio."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class DataAudit:
    rows: int
    duplicate_rows: int
    missing_by_column: dict[str, int]


def audit_frame(frame: pd.DataFrame) -> DataAudit:
    return DataAudit(
        rows=len(frame),
        duplicate_rows=int(frame.duplicated().sum()),
        missing_by_column={str(k): int(v) for k, v in frame.isna().sum().items()},
    )


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def singular_random_effect_warning(variance: float, tolerance: float = 1e-6) -> str | None:
    if variance <= tolerance:
        return ("Random-effect variance is effectively zero; interpret fixed effects only "
                "and do not publish group rankings.")
    return None
