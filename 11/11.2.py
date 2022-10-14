access_rights = {}
n = int(input('Введіть к-сть файлів для перевірки, n: '))
for i in range(n):
    l = input(f'Введіть назву файлу #{i + 1} та допустимі команди: ').split()
    access_rights[l[0]] = set(l[1:])
for k in range(int(input('Введіть к-сть запитів до файлів, m: '))):
        a_r, request = input(f'Введіть потрібну команду та назву файлу, запит #{k + 1}: ').split()
        if a_r == 'write':
            a_r = 'W'
        if a_r == 'read':
           a_r = 'R'
        if a_r == 'execute':
            a_r = 'X'
        if a_r in access_rights[request]:
            print('OK')
        else:
            print('Access denied')
