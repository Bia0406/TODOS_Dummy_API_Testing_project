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
        - the status code name is OK
        - in response we have total 150 todos
        - in response we have limit 30 todos

        """

        response = self.requests_handler.get_all_todos()
        expected_status_code = 200
        expected_api_status = "OK"
        expected_number_total_todos = 150
        expected_todos = 30
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_api_status, response.reason)
        self.assertEqual(expected_number_total_todos, response.json()["total"])
        self.assertEqual(expected_todos, response.json()["limit"])

