A = []
C = []
for i in range(5):
    number = int(input(f'Введіть число #{i + 1}: '))
    A += [number]
print(f'Список A: {A}')
for n in A:
    if n > 5:
        C.append(n)
print(f'Список C (числа > 5): {C}')
