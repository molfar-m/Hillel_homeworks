def read_last(lines, file):
    if lines < 1 or type(lines) != int:
        print('Кількість строк може бути лише цілим, додатнім числом')
    else:
        with open(file, encoding='utf-8') as k:
            file_lines = k.readlines()[-lines:]
        for j in file_lines:
            print(j.strip())


read_last(3, 'file.txt')
