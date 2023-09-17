import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodo(unittest.TestCase):

    """
    Testam ruta GET /<todo_id>
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todo_when_id_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive a todo with the specified todo_id
        """
        todo_id = 1
        response = self.requests_handler.get_single_todo_by_id(todo_id=todo_id)
        expected_status_code = 404
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(todo_id, len(response.text[1]))

    def test_get_todo_when_id_does_not_exists_in_db(self):
        """
        Check:
        - the status code is 404
        - in response I got the expected error
        """

        response = self.requests_handler.get_single_todo_by_id(todo_id=151)
        expected_status_code = 404
        expected_error = 'not found!'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.text)
