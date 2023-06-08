from requests import Response
from json.decoder import JSONDecodeError
from random import randint


class BaseCase:

    def get_id(self):
        ids = randint(1, 10)
        return ids

    def get_json(self, response: Response):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        return response_as_dict

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have a key '{name}'"

        return response_as_dict[name]
