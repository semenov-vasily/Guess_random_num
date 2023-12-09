from random import *


# Функция для создания случайного числа в диапазоне от 1 до заданного числа n
def random_num():
    n = int(input('Введите число правой границы для случайного выбора числа: '))
    num_randint = randint(1, n)
    return num_randint, n


# Функция, проверяющая, что предполагаемое число является и входит в диапазон от 1 до заданного числа n
def is_valid(num, n):
    return num.isdigit() and 0 < int(num) < (n + 1) and float(num) == int(float(num))


# Функция для ввода предполагаемого числа
def numbers(n):
    while True:
        num = input('Введите число: ')
        if is_valid(num, n):
            return int(num)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')


# Функция проверяющая, угадано число или нет
def check_numbers():
    print('Добро пожаловать в числовую угадайку!')
    num_randint, n = random_num()
    count = 0
    while True:
        num = numbers(n)
        count += 1
        if num < num_randint:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > num_randint:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали, поздравляем! Число: {num}, число попыток {count}')
            x = input('Cыграем еще? ведите y/n: ')
            if x == 'y':
                print('Продолжим!')
                check_numbers()
            elif x == 'n':
                print('До встречи!')
            break


if __name__ == '__main__':
    check_numbers()
