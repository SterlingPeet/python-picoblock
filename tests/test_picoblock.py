"""Test picoblock package."""
from picoblock.cli import main


def test_main():
    """Test main function."""
    assert main([]) == 0
