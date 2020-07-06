import unittest
from Tasks.AdvancedCalc import MyClass


class AdvancedCalc_TestCase(unittest.TestCase):
    """Тест для AdvancedCalc.py"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_advanced_calc(self):
        self.assertEqual(MyClass().advanced_calc('1+2*(3 + 4 / 2 - (1 + 2)) * 2 + 1'), 10)
        self.assertEqual(MyClass().advanced_calc('2+2*2'), 6)  #Проверяем приоритет операций
        self.assertNotEqual(MyClass().advanced_calc('2+2*2'), 8)  #Проверяем приоритет операций
        self.assertEqual(MyClass().advanced_calc('2+2*(3+5)'), 18) #Проверяем приоритет скобок
        self.assertRaises(ZeroDivisionError, MyClass().advanced_calc, '4/0') #Проверяем вызов исключения при делении на 0


if __name__ == '__main__':
    unittest.main()
