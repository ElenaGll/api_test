from requests import Response
from json.decoder import JSONDecodeError
import re


class Assertions:

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But it's present"

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_count_of_json(response: Response, expected_value):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert len(response_as_dict) == expected_value, \
            f"Expected value '{expected_value}' not equal to actual value '{len(response_as_dict)}'"

    @staticmethod
    def assert_dict_has_key(dictionary, name):
        assert name in dictionary, f"Dictionary does not have key '{name}'"

    @staticmethod
    def assert_dict_value_by_key(dictionary, name, expected_value):
        assert name in dictionary, f"Dictionary does not have key '{name}'"

        assert dictionary[name] == expected_value, \
            f"Expected value '{expected_value}' not equal to actual value '{dictionary[name]}'"

    @staticmethod
    def assert_check_email(email):
        assert re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email, re.IGNORECASE), \
            f"Invalid email"
