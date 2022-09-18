number = int(input("Введіть тризначне число:"))
reverced_number = 0
if 100 <= number <= 999:
    sign = number % 10 # Знаходжу останню цифру введеного числа
    number = number // 10 # Позбавляюсь останьої цифри у введеному числі
    reverced_number = reverced_number * 10 + sign # Збільшую розрядність шуканого числа та додаю до нього останню цифру
    sign = number % 10
    number = number // 10
    reverced_number = reverced_number * 10 + sign
    sign = number % 10
    number = number // 10
    reverced_number = reverced_number * 10 + sign
    print (reverced_number)
else:
    print ("ПОМИЛКА! Введіть ВИКЛЮЧНО тризначне число!")
