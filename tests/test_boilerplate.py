import pytest

from boilerplate.boilerplate import Boilerplate


def test_boilerplate() -> None:
    """Test the Boilerplate class."""
    boilerplate = Boilerplate(2, 2)
    assert boilerplate.x == 2
    assert boilerplate.y == 2
    assert boilerplate.add() == 4
    assert boilerplate.subtract() == 0
    assert boilerplate.multiply() == 4
    assert boilerplate.divide() == 1.0
    assert str(boilerplate) == "Boilerplate(2, 2)"
    with pytest.raises(ZeroDivisionError):
        Boilerplate(2, 0).divide()
