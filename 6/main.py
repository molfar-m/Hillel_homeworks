n = int(input('Введіть ширину трикутника, N: '))
row = 0

# 1)
"""while row <= n:
    print('*' * (n - row))
    row += 1"""

# 2)
"""while row <= n:
    print('*' * row)
    row += 1"""

# 3)
"""while row <= n:
    print((' ' * row) + '*' * (n - row))
    row += 1"""

# 4)
while row <= n:
    print((' ' * (n - row)) + '*' * row)
    row += 1
