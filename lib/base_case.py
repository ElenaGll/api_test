from requests import Response
from json.decoder import JSONDecodeError


class BaseCase:

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have a key '{name}'"

        return response_as_dict[name]
