import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestGetTodos(unittest.TestCase):

    """
    Testam ruta GET
    """

    def setUp(self):
        self.requests_handler = TodosDummyRequests()

    def test_get_all_todos(self):
        """
        Verificam:
        - status code-ul este 200
        - primim exact cate comenzi exista in baza de date
        """

        self.requests_handler.add_new_todo("Do something nice for someone I care about", True, 26)
        self.requests_handler.add_new_todo("Make own LEGO creation", False, 30)

        response = self.requests_handler.get_all_todos()
        expected_status_code = 200
        expected_number_todos = 30
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_number_todos, len(response.json()))

