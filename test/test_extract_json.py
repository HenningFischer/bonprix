import unittest
from src.extract_json import Extract_json

class Extract_json_UnitTest(unittest.TestCase):

    def test_extract_json(self):

        json_string = {'a': 'A', 'b': 'B', 'c': 'C', 'd': {'d1': 'D1', 'Foo': 'Bar'}, 'e': 'F'}

        search_key_list = ['b', 'd/Foo', 'e']

        expected_json = {'b': 'B', 'd/Foo': 'Bar', 'e': 'F', 'H': None}

        extract_json = Extract_json()

        assert extract_json.get_json_from_path(json_string, search_key_list) == expected_json