import allure
from lib.base_case import BaseCase
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Updating resource')
class TestUpdateResource(BaseCase):

    @allure.description('This tests updates existing resource')
    def test_update_resource(self):

        data = {
            "id": 1,
            "userId": 1,
            "title": "foo",
            "body": "bar"
        }

        response = Requests.put(f"/posts/{data['id']}", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(response, 'id', data['id'],
                                             f"Actual value '{self.get_json_value(response, 'id')}' "
                                             f"not equal expected value '{data['id']}'")
        Assertions.assert_json_value_by_name(response, 'userId', str(data['userId']),
                                             f"Actual value '{self.get_json_value(response, 'userId')}' "
                                             f"not equal expected value '{data['userId']}'")
        Assertions.assert_json_value_by_name(response, 'title', data['title'],
                                             f"Actual value '{self.get_json_value(response, 'title')}' "
                                             f"not equal expected value '{data['title']}'")
        Assertions.assert_json_value_by_name(response, 'body', data['body'],
                                             f"Actual value '{self.get_json_value(response, 'body')}' "
                                             f"not equal expected value '{data['body']}'")
