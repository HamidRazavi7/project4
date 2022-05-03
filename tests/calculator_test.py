"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


# this defines a test must say test_
def test_calculator_is_instance():
    """Testing the Calculator"""
    # instantiating the Calculator class
    calculator = Calculator()
    # checking that calculator variable contains an instance of Calculator class
    assert isinstance(calculator, Calculator)

def test_calculator_get_result_method():
    """Testing the Calculator"""
    calculator = Calculator()
    # this checks the calculator get result method
    assert calculator.get_result() == 0

