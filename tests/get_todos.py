import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodos(unittest.TestCase):

    """
    Testing the route GET
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_all_todos(self):
        """
        Check:
        - the status code is 200
        - in response we have todos that are in the database
        """

        response = self.requests_handler.get_all_todos()
        expected_status_code = 200
        expected_number_text_todos = 23328
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_number_text_todos, len(response.text))
