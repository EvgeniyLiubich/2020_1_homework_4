import unittest
from Tasks.AdvancedCalc import MyClass


class AdvancedCalc_test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_advanced_calc(self):
        self.assertEqual(MyClass().advanced_calc('1+2*(3 + 4 / 2 - (1 + 2)) * 2 + 1'), 10)
        self.assertEqual(MyClass().advanced_calc('2+2*2'), 6)
        self.assertNotEqual(MyClass().advanced_calc('2+2*2'), 8)
        self.assertEqual(MyClass().advanced_calc('2+2*(3+5)'), 18)
        self.assertRaises(ZeroDivisionError, MyClass().advanced_calc, '4/0')
