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
        - the status code name is OK
        - in response we have the key "id" equal with 150
        - in response we have for the key "isDeleted" value "true"
        """

        response = self.requests_handler.delete_todo(todo_id=150)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_response_key_id = 150
        expected_response_key_is_deleted = True
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_response_key_id, response.json()["id"])
        self.assertEqual(expected_response_key_is_deleted, response.json()["isDeleted"])
        self.assertTrue(response.json()["isDeleted"])

    def test_delete_todo_when_id_exists_not_in_db(self):
        """
        Check:
        - the status code is 404
        - the status code name is "Not Found"
        - in response I got the expected message
        """

        response = self.requests_handler.delete_todo(todo_id=152)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "Todo with id '152' not found"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()["message"])
