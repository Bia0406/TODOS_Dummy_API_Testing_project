import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetLimitAndSkipTodos(unittest.TestCase):

    """
    Testam ruta GET
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todos_when_limit_is_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive 20 limit todos
        """
        response = self.requests_handler.get_limit_and_skip_todos(limit=20)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[20]))

    def test_get_todos_when_limit_is_in_not_db(self):
        """
        Check:
        - the status code is 200
        -  we receive all 150 todos
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=180)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[150]))

    def test_get_todos_when_limit_is_a_negative_number(self):
        """
        Check:
        - the status code is 200
        -  we receive 148 todos
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=-2)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[-2]))

    def test_get_todos_when_limit_is_a_not_a_number(self):
        """
        Check:
        - the status code is 400
        - we receive message error in response
        """
        response = self.requests_handler.get_limit_and_skip_todos(limit="x")
        expected_status_code = 400
        expected_error = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, len(response.text[1]))

    def test_get_todos_when_skip_is_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive 30 todos default for skip 10
        """
        response = self.requests_handler.get_limit_and_skip_todos(skip=10)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[30]))

    def test_get_todos_when_skip_is_in_not_db(self):
        """
        Check:
        - the status code is 200
        -  we receive all 150 todos
        """

        response = self.requests_handler.get_limit_and_skip_todos(skip=180)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[150]))

    def test_get_todos_when_limit_and_skip_are_in_db(self):
        """
        Check:
        - the status code is 200
        - we receive 20 limit todos and skip for first 10 todos
        """
        response = self.requests_handler.get_limit_and_skip_todos(limit=20, skip=10)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[30]))

    def test_get_todos_when_limit_and_skip_are_not_in_db(self):
        """
        Check:
        - the status code is 200
        -  we receive all 150 todos
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=180,skip=160)
        expected_status_code = 200
        expected_todos_response = 1
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_todos_response, len(response.text[150]))



