import unittest
from Tasks.Like import MyClass


class TestLikeCase(unittest.TestCase):
    """Тест для Like.py"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_like(self):
        self.var = ["Alex", "Jacob", "Mark", "Max", "Alex", "Jacob", "Mark", "Max"]
        self.assertEqual(MyClass().likes(self.var), 'Alex, Jacob and 6 like this.')
        self.assertEqual(MyClass().likes(["Alex", "Jacob"]), 'Alex and Jacob like this.')
        self.assertNotEqual(MyClass().likes(["Alex", "Jacob"]), 'Alex и Jacob отметили, что им это нравится.')
        self.assertNotEqual(MyClass().likes(self.var), 'Alex, Jacob like this.')
        self.assertRaises(TypeError, MyClass().likes(self.var))
        self.assertEqual(MyClass().likes(['Петр', 'Василий']), 'Петр и Василий отметили, что им это нравится.')
        self.assertNotEqual(MyClass().likes(['Петр', 'Василий']), 'Петр and Василий like this..')


if __name__ == '__main__':
    unittest.main()
