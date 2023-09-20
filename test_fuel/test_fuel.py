from fuel import gauge
from fuel import convert
import pytest

def test_convert():
    assert convert("4/8") == 50
    assert convert("2/8") == 25
    with pytest.raises(ValueError):
        convert("8/2")
    with pytest.raises(ZeroDivisionError):
        convert("8/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"