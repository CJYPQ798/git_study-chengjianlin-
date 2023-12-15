import pytest
def test_simple_assume():
    pytest.assume(1 == -1)
    pytest.assume(True)
    pytest.assume(False)