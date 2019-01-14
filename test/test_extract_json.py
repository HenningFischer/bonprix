import json
import unittest

from extract_json import Extract_json

class Extract_json_UnitTest(unittest.TestCase):

    def setUp(self):

        self.extract_json = Extract_json()
        self.string_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': {'d1': 'D1', 'Foo': 'Bar'}, 'e': 'F'}

    def test_extract_json(self):

        json_string = json.dumps(self.string_dict)

        search_key_list = ['b', 'd/Foo', 'e', 'H']

        expected_json = {'b': 'B', 'd/Foo': 'Bar', 'e': 'F', 'H': None}

        json_expected = json.dumps(expected_json)

        solution_json = self.extract_json.get_json_from_path(json_string, search_key_list)

        assert solution_json == json_expected

        assert isinstance(solution_json, str)

    def test__compare_search_key_with_json(self):

        search_key_list_element = ['d', 'Foo']
        search_key_list_element1 = ['h']
        search_key_list_element2 = 'b'

        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element) == 'Bar'
        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element1) is None
        assert self.extract_json._compare_search_key_with_json(self.string_dict, search_key_list_element2) == 'B'
