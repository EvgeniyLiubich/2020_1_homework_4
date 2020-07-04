'''
Инженерный калькулятор
Напишите программу - инженерный калькулятор. После запуска программа открывает интерактивную оболочку, в которую можно вводить комманды:

user@machine:~$ python calc.py
Advanced calculator. Author: [Student Name], Version: 1.0.0
~ ...
Базовые требования
Программа воспринимает введённые пользователем математические выражения и правильно их интепретирует:
~ 5 + 4
9
~ 10 - 3 + 1
8
~ 2 ** 3 - 1
7
Программа знает о приоритете операторов
~ 2 + 3 * 4
14
~ 8 / 2 * 3
12
Программа поддерживает изменение приоритета при помощи скобок
~ 3 * (2 + 1)
9
~ 5 + (2 - 2 * (3 + 7))
-13
Использование eval, exec, compile запрещено.
Дополнительные баллы (каждый подпункт - 1 балл)
Программа воспринимает основные математические функции и константы:
~ sqrt(3) + ln(e) - pi
-0.4095418460209159
Программа поддерживает переменные
~ x = 5
~ x
5
~ x + 3
8
Программа поддерживает оператор ' для взятия производной простейших функций
~ x = 2
~ (x ** 3)'
12
~ sin(2 * x)'
-0.8322936730942848
Программа поддерживает объявление функций
~ f(x) = x ** 2 + tg(x)'
~ f(5)
37.427881707458354

'''


class MyClass:
    __name__ = 'Advanced calculator. Author: Liubich Evgeni, Version: 1.0.0'
    print(__name__)
    def advanced_calc(self, formula_string):
        OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                     '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
        def parse(formula_string):
            number = ''
            for s in formula_string:
                if s in '1234567890.':  # если символ - цифра, то собираем число
                    number += s
                elif number:  # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                    yield float(number)
                    number = ''
                if s in OPERATORS or s in "()":  # если символ - оператор или скобка, то выдаём как есть
                    yield s
            if number:  # если в конце строки есть число, выдаём его
                yield float(number)

        def shunting_yard(parsed_formula):
            stack = []  # в качестве стэка используем список
            for token in parsed_formula:
                # если элемент - оператор, то отправляем дальше все операторы из стека,
                # чей приоритет больше или равен пришедшему,
                # до открывающей скобки или опустошения стека.
                # здесь мы пользуемся тем, что все операторы право-ассоциативны
                if token in OPERATORS:
                    while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                        yield stack.pop()
                    stack.append(token)
                elif token == ")":
                    # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                    # а открывающую скобку выкидываем из стека.
                    while stack:
                        x = stack.pop()
                        if x == "(":
                            break
                        yield x
                elif token == "(":
                    # если элемент - открывающая скобка, просто положим её в стек
                    stack.append(token)
                else:
                    # если элемент - число, отправим его сразу на выход
                    yield token
            while stack:
                yield stack.pop()

        def calc(polish):
            stack = []
            for token in polish:
                if token in OPERATORS:  # если приходящий элемент - оператор,
                    y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
                    stack.append(OPERATORS[token][1](x, y))  # вычисляем оператор, возвращаем в стек
                else:
                    stack.append(token)
            return stack[0]  # результат вычисления - единственный элемент в стеке

        return calc(shunting_yard(parse(formula_string)))







        return result  # here we return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = input('Input Expression: ')

    result = MyClass().advanced_calc(var)

    print(result)
