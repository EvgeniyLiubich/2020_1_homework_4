import unittest
from Tasks.Flags import MyClass

class Flags_Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_flags(self):
        self.assertEqual(MyClass().flags('a'), 'Вы ввели не число')