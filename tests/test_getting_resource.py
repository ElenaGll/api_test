import allure
import pytest
from lib.base_case import BaseCase
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Getting resource')
class TestGetResource(BaseCase):

    @allure.description('This test gets resource by ID')
    @pytest.mark.parametrize('ids', ['1', '10', '22', '35'])
    def test_get_resource(self, ids):

        response = Requests.get(f'/posts/{ids}')

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'userId')
        Assertions.assert_json_has_key(response, 'id')
        Assertions.assert_json_has_key(response, 'title')
        Assertions.assert_json_has_key(response, 'body')

        self.id = self.get_json_value(response, 'id')

        Assertions.assert_json_value_by_name(response, 'id', self.id,
                                             f"Expected id: {ids}, actual id: {self.id}")

    @allure.description('This test gets all resources')
    def test_get_all_resource(self):

        response = Requests.get('/posts')

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 100)
