password = input('Будь ласка, введіть ваш пароль: ')
dig = False
low_s = False
up_s = False
special_dig = False
length = len(password)
length_c = False
grade = 0

if password in 'qwerty' or password in 'admin' or password.isspace():
    grade = 1
else:
    from string import punctuation
    for symbol in password:
        if symbol.isdigit():
            dig = True
        if symbol.islower():
            low_s = True
        if symbol.isupper():
            up_s = True
        if symbol in punctuation:
            special_dig = True
    if length >= 9:
        length_c = True
grade = dig + low_s + up_s + special_dig + 1
if grade == 5 and length_c == True:
    grade = 5
elif grade == 5 and length_c == False:
    grade = 4
print('Надійність пароля: %s з 5' % grade)
