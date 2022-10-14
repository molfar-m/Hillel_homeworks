commands = {
    'write': 'W',
    'read': 'R',
    'execute': 'X',
}
access_rights = {}
n = int(input('Введіть к-сть файлів для перевірки, n: '))
for i in range(n):
    files_input = input(f'Введіть назву файлу #{i + 1} та допустимі команди: ').split()
    access_rights[files_input[0]] = set(files_input[1:])
for k in range(int(input('Введіть к-сть запитів до файлів, m: '))):
    ar, request = input(f'Введіть потрібну команду та назву файлу, запит #{k + 1}: ').split()
    if commands[ar] in access_rights[request]:
        print('OK')
    else:
        print('Access denied')
