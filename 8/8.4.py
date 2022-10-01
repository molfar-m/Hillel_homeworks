from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice
chars = (ascii_lowercase + ascii_uppercase + digits + punctuation)
symbol_lance = int(input('Введіть довжину для генерації пароля: '))
password = ''
if symbol_lance >= 9:
    for i in range(symbol_lance):
        password += choice(chars)
    print(f'Пароль: {password}')
else:
    print('Мінімальна довжина пароля повинна складати 9 символів')
