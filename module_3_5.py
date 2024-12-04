# Создаём функцию get_multiplied_digits и параметр number в ней
def get_multiplied_digits(number):
    # Создаём переменную str_number и записываем строковое представление(str) числа number в неё
    str_number = str(number)
    # Отделение первой цифры в числе: создание переменной first
    first = int(str_number[0])
    if len(str_number) > 1:
        #Возвращаем значение first * get_multiplied_digits(int(str_number[1:]))
        return first * get_multiplied_digits(int(str_number[1:]))
    # Если же длина str_number не больше 1, тогда возвращаем оставшуюся цифру first
    elif len(str_number) <= 1:
        return int(first)

get_multiplied_digits(40203)
result = get_multiplied_digits(40203)
print(result)

