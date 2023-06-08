import allure
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Deleting resources')
class TestDeleteResource:

    @allure.description('This test delete resources')
    def test_deleting_resource(self):

        response = Requests.delete('/posts/1')

        Assertions.assert_status_code(response, 200)
