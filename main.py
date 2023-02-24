"""
Натуральные числа, не превышающие 1 000 000, у которых пятая справа цифра равна 7.
Выводит на экран четные цифры стоящие в числе справа от этой 7 (прописью).
"""
import re
regex = re.compile('^\d?7\d{4}$')

numbers_dictionary = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
    '8': 'восемь',
    '9': 'девять'
}

dividers_list = {  # разделители слов
    '',
    ' ',
    ','
    '.',
    '   ',
    '\n',
    '-',
    '_',
    ':'
}


def read_block(file):
    symbol = file.read(1)
    result = ''
    while symbol not in dividers_list:
        result += symbol
        symbol = file.read(1)

    if symbol == '':  # проверка на конец файла
        return result, True
    else:
        return result, False


with open("numbers.txt", 'r') as file:
    result = read_block(file)
    raw_value = result[0]
    end_of_file = result[1]

    while end_of_file == False:
        if raw_value:
            # проверка
            passed = regex.search(raw_value)

            if passed:  # вывод четных чисел
                selected_values = raw_value[-4:]
                result_values = []
                for value in selected_values:
                    if int(value) % 2 == 0:
                        result_values.append(value)

                result_string = ''
                for result_value in result_values:
                    result_string += numbers_dictionary[result_value] + " "
                if result_string != '':
                    print(f"{raw_value}: {result_string}")

        result = read_block(file)
        raw_value = result[0]
        end_of_file = result[1]
    else:
        print('файл пустой')
