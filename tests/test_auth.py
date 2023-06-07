import allure
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Authentication cases')
class TestAuth:

    @allure.description('This test successfully authenticate user and get token')
    def test_user_auth(self):
        data = {
            "username": "admin",
            "password": "password123"
        }

        response = Requests.post('/auth', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'token')

    @allure.description('This test check authentication with wrong password')
    def test_wrong_user_auth(self):
        data = {
            "username": "admin",
            "password": "password111"
        }

        response = Requests.post('/auth', data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_not_key(response, 'token')
