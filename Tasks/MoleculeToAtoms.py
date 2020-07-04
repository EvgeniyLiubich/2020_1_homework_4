'''
Из молекулы в атомы
Напишите функцию, которая, принимая как параметр строку - формулу молекулы, возвращала бы атомы из этой молекулы и их количество в виде Dict[str, int]:

def parse_molecule(molecule: str) -> dict:
    pass
Примеры:¶
H2O -> {H: 2, O: 1}
Mg(OH)2 -> {Mg: 1, O: 2, H: 2}
K4[ON(SO3)2]2 -> {K: 4, O: 14, N: 2, S: 4}
Замечания:
Скобки в формулах могут быть круглыми, квадратными и фигурными. Такжи они могут быть вложены друг в друга.
Индекс после скобки означает количество раз, которое повторяется каждый атом внутри скобок.
Индекс после скобки необязателен. Если его нет, значит содержимое скобок повторяется 1 раз.
'''


class MyClass:

    def parse(self, var: str) -> dict:
        '''Функция считает колличество атомов в молекуле '''
        # К сожалению, я сделал программу, которая считает правильно, если множитель не больше 10
        '''Список элементоа периодической таблицы Менделеева. Получен с помощью внешней библиотеки "mendeleev" '''
        element_for_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
                             'Cl', 'Ar',
                             'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As',
                             'Se', 'Br',
                             'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
                             'Sb',
                             'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy',
                             'Ho',
                             'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb',
                             'Bi',
                             'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf',
                             'Es',
                             'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl',
                             'Mc',
                             'Lv', 'Ts', 'Og']

        def brackets(var: str):
            '''Функция ищет номер позиции закрывающей скобки'''
            i = 0
            for n, k in enumerate(var):
                if k == '(':
                    i += 1
                    if i == 1:
                        index1 = n
                elif k == ')':
                    i -= 1
                    if i == 0:
                        index2 = n
                        break
            return index2

        def converting_brackets(var: str) -> str:
            '''Функция преобразовывает скобки в круглые'''
            var = var.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
            return var

        def reverse_var(var):
            '''Функция разворачивает список'''
            return var[::-1]

        def flip_the_brackets(var):
            '''Функция разворачивает скобки'''
            var = var.replace('(', ']')
            var = var.replace(')', '(')
            var = var.replace(']', ')')
            return var

        if isinstance(var, str):
            pass
        elif not isinstance(var, str):
            print('Вы ввели неправильный тип данных ')
            raise TypeError(' the type of incoming values does not match the expected values')

        num = str(1234567890)
        print('Формула:', var)
        var = converting_brackets(var)
        var = reverse_var(var)
        var = flip_the_brackets(var)

        lst1 = []
        flag = True
        while flag == True:
            lst1 = []
            counter = 0
            while counter < (len(var)):
                if var[counter].isdigit():
                    if var[counter + 1].isalpha():
                        lst1.append(var[counter + 1] * int(var[counter]))
                        counter += 2
                        if counter > len(var):
                            pass
                    elif var[counter + 1] == '(':
                        x = brackets(var[counter:])
                        # print('Открывающая скобка: ', counter + 1)
                        # print('Закрывающая скобка :', x + counter)
                        lst1.append(var[counter + 2:x + counter] * int(var[counter]))
                        counter += (x + counter - counter + 1)
                elif var[counter].isalpha():
                    if var[counter].istitle():
                        if not var[counter - 1].isdigit() and var[counter - 1].islower():
                            lst1.append(var[counter - 1:counter + 1])
                            counter += 1
                        else:
                            lst1.append(var[counter])
                            counter += 1
                    elif var[counter].islower():
                        counter += 1
                elif var[counter] == ')':
                    counter += 1

            zzz = lst1
            '''Преобразуем список в строку'''
            zzz_str = ','.join(zzz).replace(',', '')
            var = zzz_str
            '''Проверяем, есть ли в нашей строке числа'''
            if [s for s in var if s in num]:
                flag = True
            else:
                flag = False
        '''Переворачиваем нашу формулу обратно'''
        var = reverse_var(var)
        '''Объединяем буквы верхнего и нижнего регистра'''
        lst2 = []
        i = 0
        while i < (len(var) + 1):
            try:
                if var[i].istitle() and var[i + 1].islower():
                    lst2.append(var[i:i + 2])
                    i += 2
                elif var[i].istitle() and var[i + 1].istitle():
                    lst2.append(var[i])
                    i += 1
            except IndexError:
                lst2.append(var[i])
                break
        '''Считаем колличество атомов'''
        dict1 = {}
        for i in lst2:
            if i in element_for_table:
                dict1.setdefault(i, 0)
                dict1[i] += 1

        result = dict1

        return result


if __name__ == '__main__':
    # Here we can make console input and check how function works

    var ='K4[ON(SO3)2]2'

    result = MyClass().parse(var)

    print(result)
