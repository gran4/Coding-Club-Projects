
import unittest
from unittest.mock import patch, Mock
from file_to_test import add, multiply_then_add

def test_add():
    output = add(1, 2)
    assert output == 3

@patch("file_to_test.add")
def test_multiply_then_add(mock_add):
    mock_add.return_value = 3
    output = multiply_then_add(1, 2)
    assert output == 5
    mock_add.assert_called_once_with(1, 2)


