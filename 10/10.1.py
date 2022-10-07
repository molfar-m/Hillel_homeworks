multi_list = [1, 6, 8, 5, 4, 0, 3], [5, 7, 8, 9, 4, 2, 1], [6, 0, 7, 8, 1, 2, 5], [5, 7, 2, 7, 5, 2, 1]
print('Многомірний список:')
for row in multi_list:
    for number in row:
        print(number, end=' ')
    print()
print('Перший та останній стовбці многомірного списку:')
for row in multi_list:
    print(row[0], row[len(row) - 1])
