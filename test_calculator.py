import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers_returns_sum(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)
    
    def test_add_handles_newlines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2\n3"), 6)

    def test_add_handles_mixed_delimiters(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
    
    def test_supports_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_custom_delimiter_with_newlines_as_separator(self):
        self.assertEqual(self.calculator.add("//;\n1;2\n3"), 6)
