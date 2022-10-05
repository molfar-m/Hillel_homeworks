from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices, choice, shuffle
symbol_len = int(input('Введіть число символів для генерації пароля: '))
if symbol_len >= 4:
    chars_list = [ascii_lowercase, ascii_uppercase, digits, punctuation] * (symbol_len // 4)
    chars_list.extend(choices(chars_list, k=symbol_len % 4))
    password = ''
    for r in chars_list:
        password += choice(r)
    password = list(password)
    shuffle(password)
    mixed_password = ''
    for n in password:
        mixed_password += n
    print(mixed_password)
else:
    print('Мінімальна довжина пароля повинна складати 4 символи!')
