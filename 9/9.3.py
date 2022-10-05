A = []
for i in range(10):
    number = int(input(f'Введіть число #{i + 1}: '))
    A += [number]
print(f'Список А: {A}')
N = int(input('Введіть число N: '))
print(f'Кількість повторів числа N у списку A = {A.count(N)}')
