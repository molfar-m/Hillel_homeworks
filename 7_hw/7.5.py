print('Программа шифрует только ру/eng текст и цифры!')
str = input('Введите текст для шифрования: ')
key = int(input('Введите ключ шифрования: '))
crypted_str = ''
for a in str:
    if a.islower():
        if ord(a) in range(1072, 1104):
            a_unicode = ord(a)
            a_position = ord(a) - ord('а')
            new_position = (a_position + key) % 32
            new_unicode = new_position + ord('а')
            new_char = chr(new_unicode)
            crypted_str += new_char
        else:
            a_unicode = ord(a)
            a_position = ord(a) - ord('a')
            new_position = (a_position + key) % 26
            new_unicode = new_position + ord('a')
            new_char = chr(new_unicode)
            crypted_str += new_char
    elif a.isupper():
        if ord(a) in range(1040, 1072):
            a_unicode = ord(a)
            a_position = ord(a) - ord('А')
            new_position = (a_position + key) % 32
            new_unicode = new_position + ord('А')
            new_char = chr(new_unicode)
            crypted_str += new_char
        else:
            a_unicode = ord(a)
            a_position = ord(a) - ord('A')
            new_position = (a_position + key) % 26
            new_unicode = new_position + ord('A')
            new_char = chr(new_unicode)
            crypted_str += new_char
    elif a.isdigit():
        a_unicode = ord(a)
        a_position = ord(a) - ord('0')
        new_position = (a_position + key) % 10
        new_unicode = new_position + ord('0')
        new_char = chr(new_unicode)
        crypted_str += new_char
    else:
        crypted_str += a
print('Введенный текст: ', str)
print('Зашифрованный текст: ', crypted_str)
