import json

# стан системи
wallet = dict()

# повідомлення про помилку
command_error = "COMMAND ERROR\n"

def read_wallet():
    '''
    Відображення стану системи - доступного балансу валют та обмінного курсу UAH/USD
    '''

    # читаємо стан системи із файлу
    with open("wallet.json", "r") as f:
        content = f.read()
        # перетворюємо текст в json
        global wallet
        wallet = json.loads(content)


def write_wallet():
    '''
    Запис стану системи
    '''

    # запис стану у файл стану
    with open("wallet.json", "w") as f:
        content = json.dumps(wallet)
        f.write(content)


def check_command(command) -> bool:
    '''
    Перевірка коректності строки команди
    '''

    # читання стану системи
    read_wallet()

    # аналіз команд
    # СТОП сервісу
    if command[0] == 'STOP':
        return True
    # курс та баланс
    elif command[0] == 'COURSE':
        # перевірка кількості параметрів команди
        if len(command) != 2:
            print(command_error)
            return False
    # обмін
    elif command[0] == 'EXCHANGE':
        # перевірка кількості параметрів команди
        if len(command) != 3:
            print(command_error)
            return False
        # перевірка, що 3-й параметр - число
        try:
            float(command[2])
        except ValueError:
            print(f"INVALID AMOUNT {command[2]}\n")
            return False
    # невідома команда
    else:
        print(command_error)
        return False

    # перевірка назви валюти
    try:
        wallet[command[1]]
    except Exception:
        print(f"INVALID CURRENCY {command[1]}\n")
        return False

    # пройдені всі перевірки
    return True


def get_rate(currency):
    '''
    Обмінний курс валюти
    '''

    # відображення стану
    read_wallet()
    # курс
    return 1 / wallet['USDUAH'] if currency == 'USD' else wallet['USDUAH']


def display_course(currency):
    '''
    Відображення курсу та балансу валюти currency
    '''

    # читання стану
    read_wallet()
    # курс
    rate = get_rate(currency)
    # форматування та друк
    str_rate = remove_float_zeros(rate)
    str_available = remove_float_zeros(wallet[currency])
    print(f"RATE {str_rate}, AVAILABLE {str_available}\n")


def exchange(currency, amount):
    '''
    Обмін валюти currency в кількості amount
    '''

    # читання стану
    read_wallet()
    # курс
    rate = get_rate(currency)
    # валюта за запитом
    query_currency = 'USD' if currency == 'UAH' else 'UAH'
    # кількість валюти, на яку хочемо поміняти
    query_amount = float(amount) / rate
    str_query_amount = remove_float_zeros(query_amount)
    # перевірка доступності об'єму валюти
    available = wallet[query_currency]
    if query_amount <= available:
        # обмін
        wallet[currency] += float(amount)
        wallet[query_currency] -= query_amount
        query_rate = 1 / rate
        str_query_rate = remove_float_zeros(query_rate)
        print(f"{query_currency} {str_query_amount}, RATE {str_query_rate}\n")
        # запис стану обміну
        write_wallet()
    else:
        # не вистачає кількості в обміннику
        str_available = remove_float_zeros(available)
        print(f"UNAVAILABLE, REQUIRED BALANCE {query_currency} {str_query_amount}, AVAILABLE {str_available}\n")


def remove_float_zeros(value: float) -> str:
    '''
    Забирає нулі після плаваючої точки
    Приклад:
    10.1000 -> 10.1
    10.0 -> 10
    '''

    return '{0:.4f}'.format(value).rstrip('0').rstrip('.')


def main():
    while True:
        try:
            # очікування вводу від користувача
            input_cmd = input("COMMAND?\n>>> ").strip().upper()
            # користувач не ввів команду та натиснув Enter
            if len(input_cmd) == 0:
                print(command_error)
                continue
            # розбір команди по окремим параметрам
            command = input_cmd.split(' ')
            # аналіз команди
            if not check_command(command):
                continue
            # зупинка роботи сервісу
            if command[0] == 'STOP':
                print('SERVICE STOPPED\n')
                break
            # курс та баланс
            if command[0] == 'COURSE':
                display_course(command[1])
                continue
            # обмін
            if command[0] == 'EXCHANGE':
                exchange(command[1], command[2])
                continue
        except Exception:
            print(command_error)
            continue


if __name__ == '__main__':
    main()
