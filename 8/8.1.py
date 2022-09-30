test_string = input('Введіть строку для перевірки: ')
space = 0
dig = 0
low_s = 0
up_s = 0
for symbol in test_string:
    if symbol.isspace():
        space += 1
    if symbol.isdigit():
        dig += 1
    if symbol.islower():
        low_s += 1
    if symbol.isupper():
        up_s += 1
if space and dig and low_s and up_s >= 1:
    print('YES')
else:
    print('NO')
