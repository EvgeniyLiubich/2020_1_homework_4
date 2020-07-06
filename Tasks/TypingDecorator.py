'''
Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции следующим образом: При вызове без аргументов осуществлял
бы конвертацию параметров и возвращаемого значения в указанные типы:

@typed
def add(a: int, b: int) -> str:
    return a + b

add("3", 5) -> "8"
add(2.35, True) -> "3"
При вызове с параметром strict=True выбрасывал бы исключение при неправильной передаче параметров:

@typed(strict=True)
def convert_upper(msg: str) -> str:
    return msg.upper()

convert_upper('abc') -> 'ABC'
convert_upper(5) -> TypeError('`convert_upper` argument `msg` required to be a `str` instance')
Если типы параметров функции не указаны декоратор должен предполагать их тип как Any:

@typed
def acc(a, b, c):
    return a + b + c

acc('a', 'b', 'c') -> 'abc'
acc(5, 6, 7) -> 18
acc(0.1, 0.2, 0.4) -> 0.7000000000000001
'''


class MyClass:
    # Декоратор бы работает если его запустить вне класса, но при переносе сюда в него попадает еще один аргумент '__main__.MyClass object at 0x00000186BD6CA2B0'.... и ничего не работает =(((

    def typed(strict=False):
        def decorator(function_to_decorate):
            def wrapper(self, *args):
                dict1 = function_to_decorate.__annotations__
                print("Аргументы:", *args)
                args = list(args)
                rez = list(zip([v for v in dict1.values()], [type(el) for el in args]))
                for k, i in enumerate(rez):
                    if len(set(i)) == 1:
                        pass
                    elif len(set(i)) > 1:
                        print('Типы входных данных не совпадают с типами, указанными в аннотации.'
                              '\nСейчас преобразую в нужные типы и продолжу выполнять программу.'
                              '\nЕсли в условии включена проверка входных типов данных, то '
                              'преобразования выполняться не будут ')
                        if strict == True:
                            raise TypeError('`convert_upper` argument `msg` required to be a `str` instance')
                        else:
                            if i[0] == type(1):
                                args[k] = int(args[k])
                            if i[0] == type('1'):
                                args[k] = str(args[k])
                            if i[0] == type(1.1):
                                args[k] = float(args[k])
                            if i[0] == type(True):
                                args[k] = bool(args[k])
                print(args)
                # for i in args:
                #     print("Типы аргументы:", i, ':', type(i))
                function_to_decorate(*args)
                if 'return' in dict1:
                    if dict1['return'] != type(function_to_decorate(*args)):
                        if dict1['return'] == type(1):
                            return int(function_to_decorate(*args))
                        if dict1['return'] == type('1'):
                            return str(function_to_decorate(*args))
                        if dict1['return'] == type(1.1):
                            return float(function_to_decorate(*args))
                        if dict1['return'] == type(True):
                            return bool(function_to_decorate(*args))
                # else:
                return function_to_decorate(*args)
                # print(type(function_to_decorate(*args)))

            return wrapper

        return decorator

    @typed()
    def add(a: int, b: int) -> str:
        return a + b

    @typed(strict=True)
    def convert_upper(msg: str) -> str:
        return msg.upper()

    @typed()
    def acc(a, b, c):
        return a + b + c

if __name__ == '__main__':
    # Here we can make console input and check how function works

    a = "3"
    b = 5

    result = MyClass().add(a, b)
    print(result)

    msg = 'abc'
    result = MyClass().convert_upper(msg)
    print(result)

    a = 'a'
    b = 'b'
    c = 'c'
    result = MyClass().acc(a, b, c)
    print(result)
