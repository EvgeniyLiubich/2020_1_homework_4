'''
Мне нравится 👍
Создайте функцию, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).

def likes(*arr: str) -> str:
    pass
Примеры:

likes() -> "no one likes this"
likes("Peter") -> "Peter likes this"
likes("Jacob", "Alex") -> "Jacob and Alex like this"
likes("Max", "John", "Mark") -> "Max, John and Mark like this"
likes("Alex", "Jacob", "Mark", "Max") -> "Alex, Jacob and 2 others like this"
Бонусные очки
Функция работает на нескольких языках и кодировках - язык ответа определяется по языку входного массива.
'''


class MyClass:
    def language_definition(self, var: list) -> str:
        '''Функция определяет язык. Если язык не определен, то она возвращает английский язык'''
        var1 = ','.join(var).lower()
        for i in var1:
            if i in english:
                return 'english'
            elif i in russian:
                return 'russian'
        else:
            return 'english'

    def likes(self, var: list) -> str:
        '''Составляем английский и русский алфавит'''
        english = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        russian = [chr(x) for x in range(ord('а'), ord('а') + 32)]

        def language_definition(var: list) -> str:
            '''Функция определяет язык. Если язык не определен, то она возвращает английский язык'''
            var1 = ','.join(var).lower()
            for i in var1:
                if i in english:
                    return 'english'
                elif i in russian:
                    return 'russian'
            else:
                return 'english'

        if isinstance(var, list):
            pass
        elif not isinstance(var, list):
            print('Вы ввели неправильный тип данных ')
            raise TypeError(' the type of incoming values does not match the expected values')

        if len(var) == 0:
            if language_definition(var) == 'english':
                result = 'no one likes this.'
            elif language_definition(var) == 'russian':
                result = 'никому это не нравится.'
        if len(var) == 1:
            if language_definition(var) == 'english':
                result = var[0] + ' likes this.'
            elif language_definition(var) == 'russian':
                result = var[0] + ' отметил, что ему это нравится.'
        if len(var) == 2:
            if language_definition(var) == 'english':
                result = var[0] + ' and ' + var[1] + ' like this.'
            elif language_definition(var) == 'russian':
                result = var[0] + ' и ' + var[1] + ' отметили, что им это нравится.'
        if len(var) == 3:
            if language_definition(var) == 'english':
                result = var[0] + ', ' + var[1] + ' and ' + var[2] + ' like this.'
            elif language_definition(var) == 'russian':
                result = var[0] + ', ' + var[1] + ' и ' + var[2] + ' отметили, что им это нравится.'
        if len(var) > 3:
            others = len(var) - 2
            if language_definition(var) == 'english':
                result = var[0] + ', ' + var[1] + ' and ' + str(others) + ' like this.'
            elif language_definition(var) == 'russian':
                result = var[0] + ', ' + var[1] + ' и еще ' + str(others) + ' отметили, что им это нравится.'

        return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var = ["Alex", "Jacob", "Mark", "Max", "Alex", "Jacob", "Mark", "Max"]

    result = MyClass().likes(var)

    print(result)
