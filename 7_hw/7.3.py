from random import randint
x = randint(1, 10)
chance = 0
while chance < 3:
    find_number = int(input(f'Попытка #{chance + 1}: '))
    if 1 <= find_number <= 10:
        if find_number < x:
            print('Бери больше')
        if find_number > x:
            print('Бери меньше')
        if find_number == x:
            break
        chance += 1
    else:
        print('Введите число от 1 до 10')
if find_number == x:
    print('Ты угадал')
else:
    print('Ты исчерпал все попытки. Удачи в следующий раз!')
