import json

class Extract_json:

    def get_json_from_path(self, json_string, search_key_list):

        solution_dict = {}

        json_data = json.loads(json_string)

        for key in search_key_list:

            path_element_list = key.split("/")

            solution_dict[key] = self._compare_search_key_with_json(json_data, path_element_list)

        json_string_solution = json.dumps(solution_dict)

        return json_string_solution

    def _compare_search_key_with_json(self, json_data, path_element_list):

        for path_element_list_element in path_element_list:

            if path_element_list_element not in json_data:

                return None

            else:

                json_data = json_data[path_element_list_element]

        return json_data



