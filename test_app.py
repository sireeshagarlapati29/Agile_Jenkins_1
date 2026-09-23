from app import multiply, divide
import pytest

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 0) == 5
