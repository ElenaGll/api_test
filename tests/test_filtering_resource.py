import allure
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Filtering resources')
class TestFilterResource:

    @allure.description('This test filters existing resources')
    def test_filter_exist_resource(self):

        data = {
            "userId": 2
        }

        response = Requests.get('/posts', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 10)

    @allure.description('This test filters not existing resources')
    def test_filter_not_exist_resource(self):

        data = {
            "userId": 200
        }

        response = Requests.get('/posts', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 0)
