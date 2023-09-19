import unittest
import HtmlTestRunner

from tests.add_new_todo import TestAddNewTodo
from tests.delete_todo import TestDeleteTodo
from tests.get_limit_and_skip_todos import TestGetLimitAndSkipTodos
from tests.get_random_todo import TestGetRandomTodo
from tests.get_todo import TestGetTodo
from tests.get_all_todos import TestGetTodos
from tests.get_todos_by_user_id import TestGetTodosByUserId
from tests.update_todo import TestUpdateTodo


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()

        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetTodos),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetTodo),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetRandomTodo),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetLimitAndSkipTodos),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetTodosByUserId),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAddNewTodo),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateTodo),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteTodo)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name="Test Todos Dummy Requests Result",
            report_title="Test Todos Dummy API Report"

        )
        runner.run(tests_to_run)
