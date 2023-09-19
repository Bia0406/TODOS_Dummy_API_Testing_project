import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestUpdateTodo(unittest.TestCase):
    """
    Testing the route PATCH /<todo_id>
    Exemple of request body:
       {
    "completed": false
        }
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_update_todo_that_exists_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we have for the key "completed" value "false"
        - in response we have the key "id" equal with 1
        """

        response = self.requests_handler.update_todo(todo_id=1, completed=False)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_response_key_completed = False
        expected_response_key_id = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_response_key_completed, response.json()["completed"])
        self.assertEqual(expected_response_key_id, response.json()["id"])

    def test_update_todo_that_not_exists_in_db(self):
        """
        Check:
        - the status code is 404
        - the status code name is "Not Found"
        - in response I got the expected message
        """

        response = self.requests_handler.update_todo(todo_id=151, completed=False)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "Todo with id '151' not found"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()["message"])


