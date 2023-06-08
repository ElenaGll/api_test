import allure
from lib.base_case import BaseCase
from lib.requests import Requests
from lib.assertions import Assertions


@allure.epic('Getting nested resources')
class TestGetNestedResource(BaseCase):

    def setup_method(self):

        self.ids = self.get_id()

    @allure.description('This test gets nested comments of resources')
    def test_get_nested_comments_of_resource(self):

        response = Requests.get(f"/posts/{self.ids}/comments")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 5)

        for j in self.get_json(response):
            Assertions.assert_dict_value_by_key(j, 'postId', self.ids)
            Assertions.assert_dict_has_key(j, 'id')
            Assertions.assert_dict_has_key(j, 'name')
            Assertions.assert_dict_has_key(j, 'email')
            Assertions.assert_check_email(j['email'])
            Assertions.assert_dict_has_key(j, 'body')

    @allure.description('This test gets nested photos of albums')
    def test_nested_photos_of_resource(self):

        response = Requests.get(f"/albums/{self.ids}/photos")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 50)

        for j in self.get_json(response):
            Assertions.assert_dict_value_by_key(j, 'albumId', self.ids)
            Assertions.assert_dict_has_key(j, 'id')
            Assertions.assert_dict_has_key(j, 'title')
            Assertions.assert_dict_has_key(j, 'url')
            Assertions.assert_dict_has_key(j, 'thumbnailUrl')

    @allure.description('This test gets nested albums of users')
    def test_nested_albums_of_resource(self):

        response = Requests.get(f"/users/{self.ids}/albums")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 10)

        for j in self.get_json(response):
            Assertions.assert_dict_value_by_key(j, 'userId', self.ids)
            Assertions.assert_dict_has_key(j, 'id')
            Assertions.assert_dict_has_key(j, 'title')

    @allure.description('This test gets nested todos of users')
    def test_nested_todos_of_resource(self):

        response = Requests.get(f"/users/{self.ids}/todos")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 20)

        for j in self.get_json(response):
            Assertions.assert_dict_value_by_key(j, 'userId', self.ids)
            Assertions.assert_dict_has_key(j, 'id')
            Assertions.assert_dict_has_key(j, 'title')
            Assertions.assert_dict_has_key(j, 'completed')

    @allure.description('This test gets nested posts of users')
    def test_nested_posts_of_resource(self):

        response = Requests.get(f"/users/{self.ids}/posts")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_count_of_json(response, 10)

        for j in self.get_json(response):
            Assertions.assert_dict_value_by_key(j, 'userId', self.ids)
            Assertions.assert_dict_has_key(j, 'id')
            Assertions.assert_dict_has_key(j, 'title')
            Assertions.assert_dict_has_key(j, 'body')
