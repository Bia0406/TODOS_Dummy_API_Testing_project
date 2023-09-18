import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodosByUserId(unittest.TestCase):

    """
    Testing the route GET /user/<userId>
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todos_by_user_id_when_id_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive 5 todos
        - in response we have limit key equal with 5
        - in response we have the key userId equal with 1
        """

        response = self.requests_handler.get_all_todos_by_user_id(user_id=1)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_todos = 5
        expected_limit_key = 5
        expected_user_id = 1
        dict_todos = response.json()['todos']
        todos = dict_todos[0]
        user_id_key = todos["userId"]
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_todos, response.json()['total'])
        self.assertEqual(expected_limit_key, response.json()['limit'])
        self.assertEqual(expected_user_id, user_id_key)

    def test_get_todos_by_user_id_when_id_not_exists_in_db(self):
        """
        Check:
        - the status code is 404
        - the status code name is "Not Found"
        - in response I got the expected error
        """

        response = self.requests_handler.get_all_todos_by_user_id(user_id=151)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "User with id '151' not found"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()["message"])
