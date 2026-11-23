"""Public tests for Lab 06. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab06 as lab  # noqa: E402

def test_entropy_pure():
    assert lab.entropy([1, 1, 1, 1]) == 0
