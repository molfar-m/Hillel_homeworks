N = int(input('Введіть кількість значень списку: '))
A = []
for i in range(N):
    number = int(input(f'Введіть число #{i + 1}: '))
    A += [number]
print(f'Список А: {A}')
min_num = A[0]
max_num = A[0]
for n in A:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
print(f'Мінімальне значення зі списку = {min_num}')
print(f'Максимальне значення зі списку = {max_num}')