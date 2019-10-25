# -*- coding: utf-8 -*-
import urllib.request
# import language
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


class ReadWather:
    url = 'http://www.worldweatheronline.com/v2/rss.ashx?q='

    centralno_gor_lat = 47.902762
    centralno_gor_long = 33.336712

    dolgincevskiy_lat = 47.911894
    dolgincevskiy_long = 33.423332

    inguleckiy_lat = 47.836691
    inguleckiy_long = 33.347637

    metalurginiy_lat = 47.907298
    metalurginiy_long = 33.387372

    pokrovskiy_lat = 47.999229
    pokrovskiy_long = 33.449182

    sacsaganckiy_lat = 47.941024
    sacsaganckiy_long = 33.418222

    ternivckiy_lat = 48.145259
    ternivckiy_long = 33.555676
    # lang = language.ru_language()

    gorod_lat = 47.910365
    gorod_long = 33.391806

    def water_read(self, rayon='', how=''):
        if not rayon:
            gorod = self.return_wather(self.gorod_lat, self.gorod_long, how=how)

            return (
                    f'☀ Погода в городе {gorod}'
                )

    def return_wather(self, lat, lon, how='', test=False):
        url_query = f'{self.url}{lat},{lon}'

        try:
            url_read = urllib.request.urlopen(url_query)
        except HTTPError as e:
            if test:
                return ["HTTPError", e.code, url_query]
            else:
                return self.lang['something_went_wrong']
        except URLError as e:
            if test:
                return ["URLError", e.reason, url_query]
            else:
                return self.lang['not_possible_process']

        soup = BeautifulSoup(url_read, "html.parser")
        title = soup.findAll('title')
        current_weather = self.replace_text_wather(title[1].getText().split(': ')[1])
        today_weather = self.replace_text_wather(title[2].getText().split(': ')[1])
        tomorrow_weather = self.replace_text_wather(title[3].getText().split(': ')[1])

        description = soup.findAll('description')
        current_description_temp = description[1].getText().split('<br />')[1]
        current_description_wind = description[1].getText().split('<br />')[2]
        today_description_hide_low = description[2].getText().split('<br />')[1]
        today_description_wind = description[2].getText().split('<br />')[2]
        tomorrow_description_hide_low = description[3].getText().split('<br />')[1]
        tomorrow_description_wind = description[3].getText().split('<br />')[2]

        current_temp = current_description_temp.split('</b>')[1].split(' ')[0].replace('&deg;c', '°C')
        current_wind = current_description_wind.split('</b>')[1].split('(')[0].split(' ')
        current_wind_ukazatel = self.replace_text_wind(current_wind[0])
        current_wind_speed = "%.1f" % (float(current_wind[2]) * 2.237)

        today_temp_hide = today_description_hide_low.split('</b>')[1].split(' ')[0].replace('&deg;c', '°C')
        today_temp_low = today_description_hide_low.split('</b>')[2].split(' ')[0].replace('&deg;c', '°C')
        today_wind = today_description_wind.split('</b>')[1].split('(')[0].split(' ')
        today_wind_ukazatel = self.replace_text_wind(today_wind[0])
        today_wind_speed = "%.1f" % (float(today_wind[2]) * 2.237)

        tomorrow_temp_hide = tomorrow_description_hide_low.split('</b>')[1].split(' ')[0].replace('&deg;c', '°C')
        tomorrow_temp_low = tomorrow_description_hide_low.split('</b>')[2].split(' ')[0].replace('&deg;c', '°C')
        tomorrow_wind = tomorrow_description_wind.split('</b>')[1].split('(')[0].split(' ')
        tomorrow_wind_ukazatel = self.replace_text_wind(tomorrow_wind[0])
        tomorrow_wind_speed = "%.1f" % (float(tomorrow_wind[2]) * 2.237)

        if not how:
            result = f'Сегодня\n' \
                f'Днём: {today_temp_hide}\n' \
                f'Ночью: {today_temp_low}\n' \
                f'На улице: {today_weather}\n' \
                f'Ветер: {today_wind_ukazatel}\n' \
                f'Скорость: {today_wind_speed} м/с\n\n' \
                f'Сейчас\n' \
                f'Температура: {current_temp}\n' \
                f'На улице: {current_weather}\n' \
                f'Ветер: {current_wind_ukazatel}\n' \
                f'Скорость: {current_wind_speed} м/с\n\n' \
                f'Завтра\n' \
                f'Днём: {tomorrow_temp_hide}\n' \
                f'Ночью: {tomorrow_temp_low}\n' \
                f'На улице: {tomorrow_weather}\n' \
                f'Ветер: {tomorrow_wind_ukazatel}\n' \
                f'Скорость: {tomorrow_wind_speed} м/с'
        else:
            if how == 'today':
                result = f'сегодня\n' \
                    f'▪Днём: {today_temp_hide}\n' \
                    f'▪Ночью: {today_temp_low}\n' \
                    f'▪На улице: {today_weather}\n' \
                    f'▪Ветер: {today_wind_ukazatel}\n' \
                    f'▪Скорость: {today_wind_speed} м/с' \

            if how == 'now':
                result = f'сейчас\n' \
                    f'▪Температура: {current_temp}\n' \
                    f'▪На улице: {current_weather}\n' \
                    f'▪Ветер: {current_wind_ukazatel}\n' \
                    f'▪Скорость: {current_wind_speed} м/с' \

            if how == 'tomorrow':
                result = f'завтра\n' \
                    f'▪Днём: {tomorrow_temp_hide}\n' \
                    f'▪Ночью: {tomorrow_temp_low}\n' \
                    f'▪На улице: {tomorrow_weather}\n' \
                    f'▪Ветер: {tomorrow_wind_ukazatel}\n' \
                    f'▪Скорость: {tomorrow_wind_speed} м/с'

        return result


        # print(url_query)
        # try:
        #     url_read = urllib.request.urlopen(url_query).read()
        #     print(url_read)
        # except:
        #     return "Погода не найдено!"

        # print(current_weather)
        # print(current_temp)
        # print(current_wind_ukazatel)
        # print(f'{float(current_wind_speed) * 2.237} м/с')
        # print()
        # print(today_weather)
        # print(today_description_hide_low)
        # print(today_description_wind)
        # print(today_temp_hide)
        # print(today_temp_low)
        # print(today_wind_ukazatel)
        # print(today_wind_speed)
        # print(tomorrow_weather)
        # print(tomorrow_description_hide_low)
        # print(tomorrow_description_wind)
        # print(tomorrow_temp_hide)
        # print(tomorrow_temp_low)
        # print(tomorrow_wind)
        # print(tomorrow_wind_ukazatel)
        # print(tomorrow_wind_speed)

    @staticmethod
    def replace_text_wather(text):

        if "Sunny" in text:
            return "Солнечно"
        elif "Partly cloudy" in text:
            return "Переменная облачность"
        elif "Moderate or heavy rain in area with thunder" in text:
            return "Умеренный или сильный дождь с громом"
        elif "Clear" in text:
            return "Чисто"
        elif "Overcast" in text:
            return "Облачно"
        elif "Moderate rain" in text:
            return "Умеренный дождь"
        elif "Light rain" in text:
            return "Легкий дождь"
        elif "Light rain shower" in text:
            return "Местами небольшой дождь"
        elif "Light snow showers" in text:
            return "Легкий снег"
        elif "Heavy snow" in text:
            return "Снегопад"
        elif "Moderate or heavy snow showers" in text:
            return "Мокрый снег"
        elif "Patchy heavy snow" in text:
            return "Легкий снег"
        elif "Fog" in text:
            return "Туман"
        elif "Blowing snow" in text:
            return "Метель"
        elif "Light snow" in text:
            return "Легкий снег"
        elif "Mist" in text:
            return "Легкий туман"
        elif "Light drizzle" in text:
            return "Легкая морось"
        elif "Patchy rain nearby" in text:
            return "небольшой дождь"
        elif "Patchy rain possible" in text:
            return "дождь"
        elif "Overcast" in text:
            return "cплошная облачность"
        elif "Light rain shower" in text:
            return "местами небольшой дождь"
        elif "Light snow" in text:
            return "легкий снег"
        elif "Light snow showers" in text:
            return "лёгкий снег с дождём"
        elif "Partly cloudy" in text:
            return "переменная облачность"
        elif "Sunny" in text:
            return "ясно"
        elif "Cloudy" in text:
            return "облачно"
        elif "Moderate or heavy rain shower" in text:
            return "умеренный или сильный дождь"
        elif "Moderate or heavy rain with thunder" in text:
            return "умеренный или сильный дождь с громом"
        elif "Moderate rain at times" in text:
            return "Временами умеренный дождь"
        elif "Light drizzle" in text:
            return "возможен мелкий дождь"
        elif "Torrential rain shower" in text:
            return "проливной дождь"
        elif "Thundery outbreaks in nearby" in text:
            return "неподалёку грозовые облака"
        elif "Fog" in text:
            return "туман"
        elif "Blowing snow" in text:
            return "метель"
        elif "Overcast " in text:
            return "облачно"
        elif "Light sleet showers" in text:
            return "легкий дождь со снегом"
        elif "Light sleet" in text:
            return "легкий снег"
        else:
            return text

    @staticmethod
    def replace_text_wind(text):
        if 'N' in text:
            return 'Северный'
        elif 'E' in text:
            return 'Восточный'
        elif 'S' in text:
            return 'Южный'
        elif 'W' in text:
            return 'Западный'
        elif 'NE' in text:
            return 'Северо-Востчный'
        elif 'SE' in text:
            return 'Юго-Восточный'
        elif 'SW' in text:
            return 'Юго-Западный'
        elif 'NW' in text:
            return 'Северо-Западный'
        elif 'NNE' in text:
            return 'Северо-Северо-Востчный'
        elif 'ENE' in text:
            return 'Восточно-Северо-Востчный'
        elif 'ESE' in text:
            return 'Восточно-Юго-Востчный'
        elif 'SSE' in text:
            return 'Юго-Юго-Восточный'
        elif 'SSW' in text:
            return 'Юго-Юго-Западный'
        elif 'WSW' in text:
            return 'Западно-Юго-Западный'
        elif 'WNW' in text:
            return 'Западно-Северо-Западный'
        elif 'NNW' in text:
            return 'Северо-Северо-Западный'
        else:
            return text
