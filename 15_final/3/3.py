from datetime import datetime, date, timedelta
import yfinance as yf

# робота побудована на сервісі курсів Yahoo Finance API через модуль yfinance (треба інсталювати у пакетах)

# словник з повідомленнями про помилки
errs = {
    "system": "System Error",
    "currency": "Invalid currency name",
    "date": "Invalid date"
    }


def output(text):
    '''
    Вивід у консоль
    '''

    print('--------------')
    print(text)
    print('==============\n')


def ticker_date_price(ticker_name, dt) -> float:
    '''
    Запит ціни закриття на дату
    '''

    # запит тікеру
    ticker = yf.Ticker(ticker_name)
    try:
        # перевірка наявності тікеру на веб-сервісі
        ticker.info['symbol']
    except KeyError as e:
        raise ValueError('currency')
    # перетворення дати у строку
    str_date = ''
    if type(dt) == date:
        str_date = '{}-{}-{}'.format(dt.year, dt.month, dt.day)
    # якщо дата вже є строкою
    if type(dt) == str:
        str_date = dt
    # наступний день за днем dt
    dt_next_day = dt + timedelta(days=1)
    str_next_day = '{}-{}-{}'.format(dt_next_day.year, dt_next_day.month, dt_next_day.day)
    # завантаження історичних даних курсу
    df = ticker.history(interval='1d', start=str_date, end=str_next_day, debug=False)
    try:
        # перевіряємо, чи отримані дані за запитом на дату
        df['Close'][0]
    except Exception as e:
        raise ValueError('date')
    return df['Close'][0]


def main():
    while True:
        # назва валюти
        currency = ''
        # поточна дата
        dt = datetime.now()

        # ввод користувача
        input_cmd = input("Введіть валюту та дату у форматі yyyy-mm-dd > ").strip().upper()
        # 1 чи 2 команди: назва валюти та дата
        commands = []
        if input_cmd:
            commands = input_cmd.split(' ')
        # користувач нічого не ввів та натиснув Enter
        if len(commands) == 0:
            output(f"{errs['system']}")
            continue
        # назва валюти
        if len(commands) > 0:
            currency = commands[0]
        # дата
        try:
            if len(commands) > 1:
                # перетворення строки формату "yyyy-mm-dd" в дату
                dt = datetime.strptime(commands[1], "%Y-%m-%d")
        except ValueError as e:
            output(f"{errs['date']} {commands[1]}")
        # запит курсу
        else:
            try:
                # шуканий курс
                rate = 0
                # гривня до долару
                ticker_uahusd = "UAHUSD=X"
                rate_uahusd = ticker_date_price(ticker_uahusd, dt.date())
                if currency == 'USD':
                    rate = rate_uahusd
                # валюта до долару для визначення крос-курсу
                else:
                    ticker = f"{currency}USD=X"
                    cross = ticker_date_price(ticker, dt.date())
                    rate = rate_uahusd / cross
                output(f"{currency}\n\n{1 / rate:.4f}")
            except ValueError as e:
                # веб-сервіс не підтримує дану валюту
                if str(e) == 'currency':
                    output(f"{currency}\n\n{errs['currency']}: {currency}")
                # введена дата, на яку немає відомостей про курс
                if str(e) == 'date':
                    output(f"{errs['date']} {dt.date()}")
            except Exception as e:
                # в процесі виконання виникла помилка
                output(f"{errs['system']}")


if __name__ == '__main__':
    main()
