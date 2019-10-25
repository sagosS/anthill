from urllib.parse import quote
from bs4 import BeautifulSoup
from my_class.get_html import GetHTML

url_query: str = 'https://index.minfin.com.ua/'


def connect_minfin(query=''):
    url_read = GetHTML().get_html(url_query + query)
    if url_read:
        soup = BeautifulSoup(url_read, "html.parser")
        return soup


def minimal_salary():
    soup = connect_minfin('ua/labour/salary/min/')
    if soup:
        salary = soup.findAll('big')
        print(f"Мнимальная зарплта: {salary[0].getText()} грн.")
        # return f"Мнимальная зарплта: {(salary[0].getText())} грн."


def fuel_query():
    query = quote('Днепропетровская')
    soup = connect_minfin(f'markets/fuel/reg/{query}/')
    if soup:
        line = soup.findAll("table", {'class': 'line'})
        zebra = soup.findAll("table", {'class': 'zebra'})
        return line, zebra


def fuel_title():
    for table in fuel_query()[0]:
        rows = table.findAll('tr')

        plus95_td = rows[1].findAll('td')
        plus95 = plus95_td[2].text
        one95_td = rows[2].findAll('td')
        one95 = one95_td[2].text
        one92_td = rows[3].findAll('td')
        one92 = one92_td[2].text
        dtone_td = rows[4].findAll('td')
        dtone = dtone_td[2].text
        gasone_td = rows[5].findAll('td')
        gasone = gasone_td[2].text

        if plus95 == '0.00' and one95 == '0.00' and one92 == '0.00' and dtone == '0.00' and gasone == '0.00':
            return f'🆕На сегодня в городе удорожания топлива не намечается.'
        else:
            if float(plus95) > 0.00:
                plus95_up = f'🆖A95+ подорожает на {plus95} грн.'
            elif float(plus95) == 0.00:
                plus95_up = ''
            else:
                plus95_up = f'🆗A95+ подешевеет на {plus95} грн.'

            if float(one95) > 0.00:
                one95_up = f'🆖A95 подорожает на {one95} грн.'
            elif float(one95) == 0.0:
                one95_up = ''
            else:
                one95_up = f'🆗A95 подешевеет на {one95} грн.'

            if float(one92) > 0.00:
                one92_up = f'🆖A92 подорожает на {one92} грн.'
            elif float(one92) == 0.00:
                one92_up = ''
            else:
                one92_up = f'🆗A92 подешевеет на {one92} грн.'

            if float(dtone) > 0.00:
                dtone_up = f'🆖ДТ подорожает на {dtone} грн.'
            elif float(dtone) == 0.00:
                dtone_up = ''
            else:
                dtone_up = f'🆗ДТ подешевеет на {dtone} грн.'

            if float(gasone) > 0.00:
                gasone_up = f'🆖ГАЗ подорожает на {gasone} грн.'
            elif float(gasone) == 0.00:
                gasone_up = ''
            else:
                gasone_up = f'🆗ГАЗ подешевеет на {gasone} грн.'

            return (
                f'🆕На протяжении дня в городе возможно изменение цены на топливо:\n'
                f'{plus95_up}\n'
                f'{one95_up}\n'
                f'{dtone_up}\n'
                f'{gasone_up}\n'
            )


def text_fuel(text):
    if text == '':
        result = '00,00'
    else:
        result = text
    return result


def fuel():
    for table in fuel_query()[1]:
        rows = table.findAll('tr')
        ukrnafta_rows = rows[1].findAll('td')
        ukrna_plus95 = text_fuel(ukrnafta_rows[2].text)
        ukrna_one95 = text_fuel(ukrnafta_rows[3].text)
        ukrna_one92 = text_fuel(ukrnafta_rows[4].text)
        ukrna_dtone = text_fuel(ukrnafta_rows[5].text)
        ukrna_gasone = text_fuel(ukrnafta_rows[6].text)
        # ukrnafta_res = f'{ukrnafta_name}\tA95+: {plus95}грн.| A95: {one95}грн.| A92: {one92}грн.| ДТ: {dtone}грн.| Газ: {gasone}грн.'

        sunOil_rows = rows[2].findAll('td')
        sunOil_plus95 = text_fuel(sunOil_rows[2].text)
        sunOil_one95 = text_fuel(sunOil_rows[3].text)
        sunOil_one92 = text_fuel(sunOil_rows[4].text)
        sunOil_dtone = text_fuel(sunOil_rows[5].text)
        sunOil_gasone = text_fuel(sunOil_rows[6].text)
        # sunOil_res = f'{sunOil_name}\tA95+: {plus95}грн.| A95: {one95}грн.| A92: {one92}грн.| ДТ: {dtone}грн.| Газ: {gasone}грн.'

        okko_rows = rows[3].findAll('td')
        okko_plus95 = text_fuel(okko_rows[2].text)
        okko_one95 = text_fuel(okko_rows[3].text)
        okko_one92 = text_fuel(okko_rows[4].text)
        okko_dtone = text_fuel(okko_rows[5].text)
        okko_gasone = text_fuel(okko_rows[6].text)
        # okko_res = f'{okko_name}\tA95+: {plus95}грн.| A95: {one95}грн.| A92: {one92}грн.| ДТ: {dtone}грн.| Газ: {gasone}грн.'

        avias_rows = rows[7].findAll('td')
        avias_plus95 = text_fuel(avias_rows[2].text)
        avias_one95 = text_fuel(avias_rows[3].text)
        avias_one92 = text_fuel(avias_rows[4].text)
        avias_dtone = text_fuel(avias_rows[5].text)
        avias_gasone = text_fuel(avias_rows[6].text)
        return (f'🚗🚗🚗 Цены топлива на заправках Кривого Рога 🚕🚕🚕\n'
                f'{fuel_title()}\n'
                f'⛽Укрнафта\n▪A95+: {ukrna_plus95} | A95: {ukrna_one95} | A92: {ukrna_one92} | ДТ: {ukrna_dtone} | Газ: {ukrna_gasone}\n'
                f'⛽Sun OIL\n▪A95+: {sunOil_plus95} | A95: {sunOil_one95} | A92: {sunOil_one92} | ДТ: {sunOil_dtone} | Газ: {sunOil_gasone}\n'
                f'⛽OKKO\n▪A95+: {okko_plus95} | A95: {okko_one95} | A92: {okko_one92} | ДТ: {okko_dtone} | Газ: {okko_gasone}\n'
                f'⛽Авиас\n▪A95+: {avias_plus95} | A95: {avias_one95} | A92: {avias_one92} | ДТ: {avias_dtone} | Газ: {avias_gasone}')
