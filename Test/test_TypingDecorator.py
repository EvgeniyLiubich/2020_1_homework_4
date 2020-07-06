import unittest
from Tasks.TypingDecorator import MyClass


class TestTypingDecoratorCase(unittest.TestCase):
    """Тест для TypingDecorator.py"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typing_decorator(self):
        self.assertEqual(MyClass.add(self, '3', 5), '8')
        self.assertNotEqual(MyClass.add(self, '3', 5), 8)
        self.assertEqual(MyClass.acc(self, 'a', 'b', 'c'), 'abc')
        self.assertNotEqual(MyClass.acc(self, 'a', 'b', 'c'), 'bac')
        self.assertEqual(MyClass.acc(self, 5, 6, 7), 18)
        self.assertNotEqual(MyClass.acc(self, 5, 6, 7), '18')
        self.assertEqual(MyClass.acc(self, 0.1, 0.2, 0.4), 0.7000000000000001)
        self.assertNotEqual(MyClass.acc(self, 0.1, 0.2, 0.4), 0.7)
