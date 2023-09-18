import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetLimitAndSkipTodos(unittest.TestCase):

    """
    Testing the route GET
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_todos_when_limit_is_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive 20 todos, that is exactly the set limit
        - in response we have total equal with 150
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=20)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_todos = 20
        expected_number_total_todos = 150
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_todos, len(response.json()["todos"]))
        self.assertEqual(expected_number_total_todos, response.json()["total"])

    def test_get_todos_when_limit_is_in_not_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive 150 todos limit, different from the set limit
        - in response we have total equal with 150
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=180)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_todos = 150
        expected_total_key = 150
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_todos, len(response.json()["todos"]))
        self.assertEqual(expected_total_key, response.json()["total"])

    def test_get_todos_when_limit_is_a_negative_number(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive 148 todos limit, different from the set limit
        - in response we have total equal with 150
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=-2)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_todos_response = 148
        expected_total_key = 150
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_todos_response, len(response.json()["todos"]))
        self.assertEqual(expected_total_key, response.json()["total"])

    def test_get_todos_when_limit_is_a_not_a_number(self):
        """
        Check:
        - the status code is 400
        - the status code name is 'Bad Request'
        - in response I got the expected error
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit="x")
        expected_status_code = 400
        expected_response_status = "Bad Request"
        expected_error = "Invalid limit"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_error, response.json()['message'])

    def test_get_todos_when_skip_is_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - we receive 30 todos because of the limit default, but skip first 10 todos
        """

        response = self.requests_handler.get_limit_and_skip_todos(skip=10)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_todos_response = 30
        expected_total_key = 150
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_todos_response, len(response.json()["todos"]))
        self.assertEqual(expected_total_key, response.json()["total"])

    def test_get_todos_when_skip_is_in_not_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we receive all the total key with value 150 and ignoring the set limit 180
        - the key skip is 180 in response
        - in response we receive a list by todos key
        """

        response = self.requests_handler.get_limit_and_skip_todos(skip=180)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_total_key = 150
        expected_key_skip = 180
        expected_todos = []
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_total_key, response.json()["total"])
        self.assertEqual(expected_key_skip, response.json()['skip'])
        self.assertEqual(expected_todos, response.json()['todos'])

    def test_get_todos_when_limit_and_skip_are_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we have key total equal with 150
        - in response we receive 20 todos, that is exactly the limit set
        - the key skip is 10 in response, that is exactly the skip set
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=20, skip=10)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_total_key = 150
        expected_todos = 20
        expected_key_skip = 10
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_total_key, response.json()["total"])
        self.assertEqual(expected_todos, response.json()['limit'])
        self.assertEqual(expected_key_skip, response.json()['skip'])

    def test_get_todos_when_limit_and_skip_are_not_in_db(self):
        """
        Check:
        - the status code is 200
        - the status code name is OK
        - in response we have key total equal with 150
        - the key skip is 160 in response, that is exactly the skip set
        - in response the limit key is 0, different from the set limit
        - in response we receive a list by todos key
        """

        response = self.requests_handler.get_limit_and_skip_todos(limit=180, skip=160)
        expected_status_code = 200
        expected_response_status = "OK"
        expected_total_key = 150
        expected_key_skip = 160
        expected_limit_key = 0
        expected_todos = []
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_response_status, response.reason)
        self.assertEqual(expected_total_key, response.json()["total"])
        self.assertEqual(expected_key_skip, response.json()['skip'])
        self.assertEqual(expected_limit_key, response.json()['limit'])
        self.assertEqual(expected_todos, response.json()['todos'])



