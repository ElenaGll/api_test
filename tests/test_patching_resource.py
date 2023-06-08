import allure
from lib.base_case import BaseCase
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Patching resources')
class TestPatchResource(BaseCase):

    @allure.description('This test patches a title in a resource')
    def test_patching_title_in_resource(self):

        data = {
            "title": "foo"
        }

        response = Requests.patch('/posts/1', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, 'title', data['title'],
                                             f"Actual value '{self.get_json_value(response, 'title')}' "
                                             f"not equal expected value '{data['title']}'")

    @allure.description('This test patches a body in a resource')
    def test_patching_body_in_resource(self):

        data = {
            "body": "bar"
        }

        response = Requests.patch('/posts/1', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, 'body', data['body'],
                                             f"Actual value '{self.get_json_value(response, 'body')}' "
                                             f"not equal expected value '{data['body']}'")
