import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodo(unittest.TestCase):

    """
    Testing the route GET /<todo_id>
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todo_when_id_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we have the todo id equal with 1
        """

        todo_id = 1
        response = self.requests_handler.get_single_todo_by_id(todo_id=todo_id)
        expected_status_code = 200
        expected_response_status = "OK"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(todo_id, response.json()['id'])

    def test_get_todo_when_id_does_not_exists_in_db(self):
        """
        Check:
        - the status code is 404
        - the status code name is 'Not Found'
        - in response I got the expected error
        """

        response = self.requests_handler.get_single_todo_by_id(todo_id=151)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "Todo with id '151' not found"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()['message'])
