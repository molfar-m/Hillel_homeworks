multi_list = [1, 6, 8, 5, 4, 0, 3], [5, 7, 8, 9, 4, 2, 1], [6, 0, 7, 8, 1, 2, 5], [5, 7, 2, 7, 5, 2, 1]
print('Многомірний список:')
for row in multi_list:
    for number in row:
        print(number, end=' ')
    print()
print('Парні стовбці, у який перший елемент > за останній:')
for s in range(len(multi_list)):
    print()
    for number in range(len(multi_list[s])):
        if number % 2 == 0 and multi_list[0][number] > multi_list[-1][number]:
            print(multi_list[s][number], end=' ')
