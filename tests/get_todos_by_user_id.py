import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodosByUserId(unittest.TestCase):

    """
    Testam ruta GET /user/<todo_id>
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todos_by_user_id_when_id_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive a todo with the specified todo_id
        """
        response = self.requests_handler.get_all_todos_by_user_id(user_id=1)
        expected_status_code = 404
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[1]))

    def test_get_todos_by_user_id_when_id_not_exists_in_db(self):
        """
        Check:
        - the status code is 404
        - in response I got the expected error
        """

        response = self.requests_handler.get_all_todos_by_user_id(user_id=151)
        expected_status_code = 404
        expected_error = 'not found!'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.text)
