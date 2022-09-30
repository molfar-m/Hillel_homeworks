# Оценка сложности пароля:
# 1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой, или пароль, содержащий меньше 9 символов
# 2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре от 9 символов
# 3 - у пользователя есть буквы в (нижнем или верхнем регистре) и цифры от 9 символов
# 4 - у пользователя есть цифры, буквы нижнего и верхнего регистра от 9 символов
# 5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов

password = input('Будь ласка, введіть ваш пароль: ')
dig = False
low_s = False
up_s = False
special_dig = False

# Пошук символів
from string import punctuation
for symbol in password:
    if symbol.isdigit():
        dig = True
    if symbol.islower():
        low_s = True
    if symbol.isupper():
        up_s = True
    if symbol in punctuation:
        special_dig = True

# Перевірка довжини пароля
length = len(password)
if length >= 9:
    length = True
else:
    length = False

# Оцінка результату
grade = dig + low_s + up_s + special_dig + length
if password in '1234567890987654321qwerty1234567890adminadminadmin123':
    grade = 1
print('Надійність пароля: %s з 5' % grade)
