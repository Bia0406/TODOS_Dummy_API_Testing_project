import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestAddNewTodo(unittest.TestCase):
    """
    Testing the route POST /add
    Exemple of request body:
       {
    "todo": "Use DummyJSON in the project",
    "completed": false,
    "userId": 5
        }
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_todo_when_user_id_is_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive a todo with a new id(next id = 151)
        - in response we have the key userId equal with 5, exactly as in the request body
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=5)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_id = 151
        expected_user_id = 5
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_id, response.json()["id"])
        self.assertEqual(expected_user_id, response.json()["userId"])

    def test_todo_when_user_id_is_not_in_db(self):
        """
        Check:
        - the status code is 404
        - the status code name is "Not Found
        - in response we receive the expected error
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=160)
        expected_status_code = 404
        expected_response_status = "Not Found"
        expected_error = "User with id '160' not found"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()["message"])

    def test_todo_when_user_id_is_null(self):
        """
        Check:
        - the status code is 400
        - the status code name is "Bad Request"
        - in response I got the expected error
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=0)
        expected_status_code = 400
        expected_response_status = "Bad Request"
        expected_error = "User id is required"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()["message"])


