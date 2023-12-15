import pytest
@pytest.mark.run(order=2)
def test_foo():
    assert True
    print("第一个")

@pytest.mark.run(order=1)
def test_bar():
    assert True
    print("第二个")
