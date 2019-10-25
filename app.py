# -*- coding: utf-8 -*-
from sys import argv
from my_function import weather, torgi_resurs, minfin, coin, holiday
from my_class import facebook, telegram

fb = facebook.Facebook()
tg = telegram.Telegram()

if argv[1] == "startDay":
    fb.picture_facebook('newDay.png', "StartDay")
elif argv[1] == "WVCF":
    weather = weather.ReadWather().water_read(how='today')
    valuta = torgi_resurs.return_valuta()
    coin = coin.coin_now()
    fuel = minfin.fuel()
    fb.text_facebook(fuel, "flue()")
    tg.text_telegram(fuel, "flue()")
    fb.text_facebook(coin, "coin()")
    tg.text_telegram(coin, "coin()")
    fb.text_facebook(valuta, "valuta()")
    tg.text_telegram(valuta, "valuta()")
    fb.text_facebook(weather, "weather()")
    tg.text_telegram(weather, "weather()")
elif argv[1] == "weatherToday":
    weather = weather.ReadWather().water_read(how='today')
    tg.text_telegram(weather, "Weather today")
    fb.text_facebook(weather, "Weather today")
elif argv[1] == "weatherNow":
    weather = weather.ReadWather().water_read(how='now')
    fb.text_picture_facebook(weather, 'shortPostWeather.png', "Weather now")
    tg.text_telegram(weather, "Weather now")
elif argv[1] == "weatherTomorrow":
    weather = weather.ReadWather().water_read(how='tomorrow')
    fb.text_facebook(weather, "Weather tomorrow")
    tg.text_telegram(weather, "Weather tomorrow")
elif argv[1] == "valuta":
    valuta = torgi_resurs.return_valuta()
    fb.text_facebook(valuta, "Valuta")
    tg.text_telegram(valuta, "Valuta")
elif argv[1] == "coin":
    coin = coin.coin_now()
    fb.text_facebook(coin, "Coin")
    tg.text_telegram(coin, "Coin")
elif argv[1] == "fuel":
    fuel = minfin.fuel()
    fb.text_facebook(fuel, "fuel")
    tg.text_telegram(coin, "fuel")
elif argv[1] == "holidayNow":
    holiday = holiday.holiday()
    if holiday:
        fb.text_facebook(holiday, "holidayNow")
        tg.text_telegram(holiday, "holidayNow")
elif argv[1] == "holidayPre":
    holiday = holiday.holiday_pre_one()
    if holiday:
        fb.text_facebook(holiday, "holidayPre")
        tg.text_telegram(holiday, "holidayPre")

