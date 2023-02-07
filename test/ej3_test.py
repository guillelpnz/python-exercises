import unittest
from ejs import ej3
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

class TestSum(unittest.TestCase):
    source_language = "en-gb"
    target_language = 'es-es'

    def test_try_endpoint_happy_path(self):
        sample_input = "flower"

        url = "https://od-api.oxforddictionaries.com:443/api/v2/translations/" + TestSum.source_language + "/" + TestSum.target_language + "/" + sample_input.lower()
        actual = ej3.try_endpoint(url, APP_ID, APP_KEY, sample_input)
        expected = ("La palabra inglesa 'flower' se puede traducir como 'flor'", [{'text': 'no flowers by request', 'translations': [{'language': 'es', 'text': 'se ruega no enviar ofrendas florales', 'type': 'direct'}]}, {'text': 'to be in floweruncountable', 'translations': [{'language': 'es', 'text': 'estar en flor', 'type': 'direct'}]}, {'text': 'flower shop', 'translations': [{'grammaticalFeatures': [{'id': 'feminine', 'text': 'Feminine', 'type': 'Gender'}], 'language': 'es', 'text': 'floristería', 'type': 'direct'}, {'grammaticalFeatures': [{'id': 'feminine', 'text': 'Feminine', 'type': 'Gender'}], 'language': 'es', 'regions': [{'id': 'latin_america', 'text': 'Latin America'}], 'text': 'florería', 'type': 'direct'}]}])

        self.assertEqual(actual, expected, f"Should be {expected}")

if __name__ == '__main__':
    unittest.main()