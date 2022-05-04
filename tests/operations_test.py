"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator add"""
    calculator = Calculator()
    # this is show using the calculator object add method
    assert calculator.add(1, 1) == 2

def test_my_first_test_add():
    """Testing the simplest addition"""
    assert 1 + 1 == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(1, 1) == 0

def test_my_first_test_subtract():
    """Testing the simplest subtraction"""
    assert 1 - 1 == 0
