import allure
from lib.base_case import BaseCase
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Creating resource')
class TestCreateResource(BaseCase):

    @allure.description('This tests creates new resource')
    def test_create_resource(self):

        data = {
            "userId": 10,
            "title": "foo",
            "body": "bar"
        }

        response = Requests.post('/posts', data=data)

        Assertions.assert_status_code(response, 201)
        Assertions.assert_json_value_by_name(response, 'userId', str(data['userId']),
                                             f"Actual value '{self.get_json_value(response, 'userId')}' "
                                             f"not equal expected value '{data['userId']}'")
        Assertions.assert_json_value_by_name(response, 'title', data['title'],
                                             f"Actual value '{self.get_json_value(response, 'title')}' "
                                             f"not equal expected value '{data['title']}'")
        Assertions.assert_json_value_by_name(response, 'body', data['body'],
                                             f"Actual value '{self.get_json_value(response, 'body')}' "
                                             f"not equal expected value '{data['body']}'")
