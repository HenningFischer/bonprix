import json

class Extract_json:

    # first convert json_data into dict
    # second take every key from search_list and split them with "/" to get a list of key_elements(path_element_list)
    # give json_data and path_element_list to compare method and get a solution dict
    # give solution_dict to convert method and return the solution_json
    def get_json_from_path(self, json_string, search_key_list):

        solution_dict = {}

        dict_data = self._convert_json_to_dict(json_string)

        for key in search_key_list:

            path_element_list = key.split("/")

            solution_dict[key] = self._compare_search_key_with_json(dict_data, path_element_list)

        json_string_solution = self._convert_dict_to_json(solution_dict)

        return json_string_solution

    # take every path_element and check if it is a key in json_data
    # if not it returns the value None
    # if yes goes into value of dict_data[key]
    def _compare_search_key_with_json(self, dict_data, path_element_list):

        for path_element_list_element in path_element_list:

            if path_element_list_element not in dict_data:

                return None

            else:

                dict_data = dict_data[path_element_list_element]

        return dict_data

    def _convert_json_to_dict(self, json_string):

        return json.loads(json_string)

    def _convert_dict_to_json(self, solution_dict):

        return json.dumps(solution_dict)


