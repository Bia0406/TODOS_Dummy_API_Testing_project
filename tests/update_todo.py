import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestUpdateTodo(unittest.TestCase):
    """
    Testam ruta PATCH /<todo_id>
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
        - we receive the update todo
        """

        response = self.requests_handler.update_todo(todo_id=1, completed=False)
        expected_status_code = 404
        expected_todo_response = "!"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todo_response, response.text[1])

    def test_update_todo_that_not_exists_in_db(self):
        response = self.requests_handler.update_todo(todo_id=151, completed=False)
        expected_status_code = 404
        expected_todo_response = "!"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todo_response, response.text[1])


