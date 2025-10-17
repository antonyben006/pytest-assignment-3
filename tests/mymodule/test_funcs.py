import pytest

from myapp.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.custom_test
def test_student_id_63():
    # Custom test for student ID ending in 63
    assert multiply(9, 7) == 63  # Changed back from 99 to 63

