import unittest

from api_requests.todos_dummy_requests import TodosDummyRequests


class TestAddNewTodo(unittest.TestCase):
    """
    Testam ruta POST /add
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
        - we receive a todo with a new id(next id = 151)
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=5)
        expected_status_code = 404
        expected_id_todo = 'l'
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_id_todo, response.text[151])

    def test_todo_when_user_id_is_not_in_db(self):
        """
        Check:
        - the status code is 404
        - in response I got the expected error
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=160)
        expected_status_code = 404
        expected_error = ('<!DOCTYPE html>\n'
                        '<html lang="en">\n'
                        '<head>\n'
                        '<meta charset="utf-8">\n'
                        '<title>Error</title>\n'
                        '</head>\n'
                        '<body>\n'
                        '<pre>Cannot POST /docs/todos/add</pre>\n'
                        '</body>\n'
                        '</html>\n')
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.text)

    def test_todo_when_user_id_is_null(self):
        """
        Check:
        - the status code is 400
        - in response I got the expected error
        """

        response = self.requests_handler.add_new_todo(todo="Use DummyJSON in the project", completed=False, userId=0)
        expected_status_code = 404
        expected_error = "<"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_error, response.text[0])


