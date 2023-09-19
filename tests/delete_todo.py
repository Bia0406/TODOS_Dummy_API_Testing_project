import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestDeleteTodo(unittest.TestCase):

    """
    Testing the route DELETE /<todo_id>
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_delete_todo_when_id_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive a todo with the specified todo_id
        """

        response = self.requests_handler.delete_todo(todo_id=150)
        expected_status_code = 404
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[1]))

    def test_delete_todo_when_id_exists_not_in_db(self):
        """
        Check:
        - the status code is 404
        - in response I got the expected error
        """

        response = self.requests_handler.delete_todo(todo_id=151)
        expected_status_code = 404
        expected_error = '!'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.text[1])
