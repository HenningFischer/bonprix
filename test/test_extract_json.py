import json
import unittest

from extract_json import Extract_json

class Extract_json_UnitTest(unittest.TestCase):

    def setUp(self):

        self.extract_json = Extract_json()
        self.string_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': {'d1': 'D1', 'Foo': 'Bar'}, 'e': 'F'}
        self.json_data = json.dumps(self.string_dict)
        self.dict_data = json.loads(self.json_data)

    def test_extract_json(self):

        search_key_list = ['b', 'd/Foo', 'e', 'H']

        expected_json = {'b': 'B', 'd/Foo': 'Bar', 'e': 'F', 'H': None}

        json_expected = json.dumps(expected_json)

        solution_json = self.extract_json.get_json_from_path(self.json_data, search_key_list)

        assert solution_json == json_expected

        assert isinstance(solution_json, str)

    def test__compare_search_key_with_json(self):

        search_key_list_element = ['d', 'Foo']
        search_key_list_element1 = ['h']
        search_key_list_element2 = 'b'

        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element) == 'Bar'
        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element1) is None
        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element2) == 'B'

    def _convert_json_to_dict(self):

        assert isinstance(self.extract_json._convert_json_to_dict(self.json_data), object)
    
    def _convert_dict_to_json(self):

        assert isinstance(self.extract_json._convert_dict_to_json(self.dict_data), dict)
