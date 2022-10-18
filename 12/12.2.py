from json import dump
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = dict.copy(A)
for i, j in B.items():
    if not C.get(i):
        C[i] = j
    else:
        C[i] = [C[i], j]
with open('result.json', 'w') as k:
    dump(C, k)
