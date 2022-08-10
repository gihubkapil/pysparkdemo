import pytest
from app.main import *


def test_capital_letter():
    assert capital_case('semaphore') == 'Semaphore'


def test_raise_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)