import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from open_data.diagnostics import audit_frame, file_sha256, singular_random_effect_warning


class DiagnosticsTest(unittest.TestCase):
    def test_audit(self):
        audit = audit_frame(pd.DataFrame({"x": [1, 1, None]}))
        self.assertEqual(audit.rows, 3)
        self.assertEqual(audit.missing_by_column["x"], 1)

    def test_hash_and_warning(self):
        with tempfile.NamedTemporaryFile() as handle:
            handle.write(b"data")
            handle.flush()
            self.assertEqual(len(file_sha256(handle.name)), 64)
        self.assertIsNotNone(singular_random_effect_warning(0.0))


if __name__ == "__main__":
    unittest.main()
