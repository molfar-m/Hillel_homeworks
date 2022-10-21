def change(lst):
    if len(lst) < 2:
        print('Error! Список має містити щонайменше два елементи!')
        exit()
    else:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst


print(change(['volodymyr', 2, 'w', 4, 100]))
