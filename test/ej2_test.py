import unittest
from ejs.ej2 import delete_zeros

class TestSum(unittest.TestCase):

    def test_delete_zeros_happy_path(self):
        sample_input = "210.010.090.180"
        
        expected = "210.10.90.180"
        actual = delete_zeros(sample_input)

        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_delete_zeros_invalid_string(self):
        sample_input = "Invalid string"

        actual = delete_zeros(sample_input)

        self.assertIsNone(actual, "Should be None")

    def test_delete_zeros_empty_string(self):
        sample_input = ""

        actual = delete_zeros(sample_input)

        self.assertIsNone(actual, "Should be None")

    def test_delete_zeros_wrong_type(self):
        sample_input = 9

        actual = delete_zeros(sample_input)

        self.assertIsNone(actual, "Should be None")

if __name__ == '__main__':
    unittest.main()