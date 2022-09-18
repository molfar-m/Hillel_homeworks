a = float(input('Введіть число a:'))
b = float(input('Введіть число b:'))
c = float(input('Введіть число c:'))
max = a
if max != b or max != c:
    if b > max:
        max = b
    if c > max:
        max = c
    print('Найбільше число', max)
else:
    print('Усі три числа рівні між собою')