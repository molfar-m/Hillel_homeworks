N = int(input('Введіть кількість значень списку: '))
A = []
for i in range(N):
    number = int(input(f'Введіть число #{i + 1}: '))
    A += [number]
print(f'Список А: {A}')
A.reverse()
print(f'Список А з оберненою послідовністю: {A}')