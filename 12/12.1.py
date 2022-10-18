from pickle import dump
dictionary_list = [
    {
        'name': 'Ivan',
        'age': 30,
        'job': 'teacher'
    },
    {
        'name': 'Anton',
        'age': 35,
        'job': 'manager'
    },
    {
        'name': 'Olha',
        'age': 29,
        'job': 'accountant'
    }
]
with open('study.hillel', 'wb') as k:
    dump(dictionary_list, k)
