import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetRandomTodo(unittest.TestCase):

    """
    Testam ruta GET /random
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_a_random_todo(self):
        """
        Check:
        - the status code is 200
        - we receive a todo every time random id and userId
        """
        response = self.requests_handler.get_todo_by_random()
        expected_status_code = 404
        expected_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response, len(response.text[1]))
