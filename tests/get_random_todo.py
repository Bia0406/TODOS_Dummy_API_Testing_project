import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetRandomTodo(unittest.TestCase):

    """
    Testing the route GET /random
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_a_random_todo(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we have 4 key - value
        - in response we have the key 'id'
        """

        response = self.requests_handler.get_todo_by_random()
        expected_status_code = 200
        expected_response_status = "OK"
        expected_key_value = 4
        expected_key = "id"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_key_value, len(response.json()))
        self.assertIn(expected_key, response.json())

