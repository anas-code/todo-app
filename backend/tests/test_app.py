import unittest
from app import app

class TodoAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.tasks = []
    def test_get_tasks(self):
        pass

    def test_add_task(self):
        pass

    def test_delete_task(self):
        pass

    def test_complete_task(self):
        pass

if __name__ == '__main__':
    unittest.main()
