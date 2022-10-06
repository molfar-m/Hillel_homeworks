text = input('Введіть текст для підрахунку цифр:')
num_list = []
num = ''
for char in text:
    if char.isdigit():
        num += char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
if num != '':
    num_list.append(int(num))
print(f'Кількість цифр: {len(num_list)}')
