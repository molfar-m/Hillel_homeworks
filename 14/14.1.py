import copy
data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]

data_copy = copy.deepcopy(data)
print(data_copy)


def delete_item(position: int) -> list:
    global data_copy
    for i in range(len(data_copy)):
        if i + 1 == position:
            data_copy.pop(i)
            break
    data_copy = sorted(data_copy, key=lambda x: x['position'])
    for j in range(len(data_copy)):
        data_copy[j]['position'] = j + 1
    return [list]


def add_item(name: str, position: int) -> list:
    global data_copy
    data_copy.insert(0, {'name': name, 'position': position})
    data_copy = sorted(data_copy, key=lambda x: x['position'])
    for i in range(len(data_copy)):
        data_copy[i]['position'] = i + 1
    return [list]


def change_item(position1: int, position2: int) -> list:
    global data_copy
    for i in range(len(data_copy)):
        if i + 1 == position1:
            data_copy[i]['position'] = position2
        if i + 1 == position2:
            data_copy[i]['position'] = position1
    data_copy = sorted(data_copy, key=lambda x: x['position'])
    for j in range(len(data_copy)):
        data_copy[j]['position'] = j + 1
    return [list]


# delete_item(2)
# print(data_copy)
# add_item('Test 4', 1)
# print(data_copy)
change_item(1, 3)
print(data_copy)
