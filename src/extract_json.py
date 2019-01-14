
class Extract_json:

    def get_json_from_path(self, json_string, search_key_list):

        solution_dict = {}

        for key in search_key_list:

            path_element_list = key.split("/")

            solution_dict[key] = self._compare_search_key_with_json(json_string, path_element_list)

    def _compare_search_key_with_json(self, json_string, path_element_list):

                if len(path_element_list) == 1:

                    return json_string[path_element_list]

                self._compare_search_key_with_json(json_string[path_element_list[0]], path_element_list.pop(0))



