# -*- coding: utf-8 -*-
from my_class import dbhelper, get_html
from bs4 import BeautifulSoup

db = dbhelper.DBHelper()
db.setup()
url_query = 'https://relax.com.ua/holidays'


def connect_holidays(query=''):
    url_read = get_html.GetHTML().get_html(url_query + query)
    if url_read:
        soup = BeautifulSoup(url_read, "html.parser")
        return soup


def read_holidays():
    soup = connect_holidays()
    if soup:
        # запрос кол-во страниц
        last = int(soup.find("a", {'class': 'last'})['href'].split('/')[5])
        i = 1
        while i <= last:
            if i == 1:
                # если первая страница запрос типа https://relax.com.ua/holidays
                soup = connect_holidays()
                # ищем все плашки праздников
                soup = soup.findAll("a", {'class': 'info-item-light holiday-item'})
                for item in soup:
                    # print(item)
                    # название праздника
                    holidays_title = item.find('div', {'class': 'post-box-title'}).get_text()
                    print(holidays_title)
                    # ссылка на страницу с описанием праздника
                    holidays_href = item['href'].split('/')[4]
                    href = '/' + holidays_href + '/'
                    # print(href)
                    # ссылка на картинку праздника
                    holidays_img = item.find('div', {'class': 'post-thumbnail-wide'})
                    img = holidays_img['style'].split('\'')[1]
                    print(img)
                    # дата празднования
                    holidays_data = item.find('div', {'class': 'time-block'}).get_text().split(': ')[1].split('.')
                    data = holidays_data[0] + '.' + holidays_data[1]
                    print(data)
                    # входим на страницу описания
                    # TODO: проблема с кодировкой UTF-8, помогает отключение в get_html
                    soup = connect_holidays(href)
                    soup = soup.find('div', {'class': 'text'}).findAll('p')
                    # проверяем на странице много тегов "p" или один
                    if soup:
                        # print(soup)
                        text = ''
                        for p in soup:
                            # получаем текст
                            text += p.get_text()
                            # print(text)
                    else:
                        soup = soup.find('div', {'class': 'text'}).find('p')
                        text = ''
                        # получаем текст
                        text += soup.get_text()
                    # пишем данные в базу
                    db.check_holidays_in_db(data, holidays_title, text, img)
                    print('')
            else:
                # если первая страница запрос типа https://relax.com.ua/holidays/ссылка на страницу праздника/
                soup = connect_holidays('/page/' + str(i))
                # ищем все плашки праздников
                soup = soup.findAll("a", {'class': 'info-item-light holiday-item'})
                for item in soup:
                    # print(item)
                    # название праздника
                    holidays_title = item.find('div', {'class': 'post-box-title'}).get_text()
                    print(holidays_title)
                    # ссылка на страницу с описанием праздника
                    holidays_href = item['href'].split('/')[4]
                    href = '/' + holidays_href + '/'
                    # print(href)
                    # ссылка на картинку праздника
                    holidays_img = item.find('div', {'class': 'post-thumbnail-wide'})
                    img = holidays_img['style'].split('\'')[1]
                    print(img)
                    # дата празднования
                    holidays_data = item.find('div', {'class': 'time-block'}).get_text().split(': ')[1].split('.')
                    data = holidays_data[0] + '.' + holidays_data[1]
                    print(data)
                    # входим на страницу описания
                    soup = connect_holidays(href)
                    soup = soup.find('div', {'class': 'text'}).findAll('p')
                    # проверяем на странице много тегов "p" или один
                    if soup:
                        # print(soup)
                        text = ''
                        for p in soup:
                            # получаем текст
                            text += p.get_text()
                            # print(text)
                    else:
                        soup = soup.find('div', {'class': 'text'}).find('p')
                        text = ''
                        # получаем текст
                        text += soup.get_text()
                    # пишем данные в базу
                    db.check_holidays_in_db(data, holidays_title, text, img)
                    print('')
            i += 1


read_holidays()
