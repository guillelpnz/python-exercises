import unittest
from ejs import ej1 

class TestSum(unittest.TestCase):

    def test_sum_string_happy_path(self):
        sample_input = "Frogtek se fundó en 2010 y ahora tiene 40 empleados"
        
        expected = 2050
        actual = ej1.sum_string(sample_input)

        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_sum_string_no_numbers(self):
        sample_input = "Frogtek desarrolla un software para la gestión de tiendas de barrio"

        expected = 0
        actual = ej1.sum_string(sample_input)

        self.assertEqual(actual, expected, "Should be None")

    def test_sum_string_negative_numbers(self):
        sample_input = "-50€ + 30€ es una operación"

        expected = -20
        actual = ej1.sum_string(sample_input)

        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_sum_string_wrong_type(self):
        sample_input = 100

        actual = ej1.sum_string(sample_input)

        self.assertIsNone(actual, "Should be None")

if __name__ == '__main__':
    unittest.main()