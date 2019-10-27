# -*- coding: utf-8 -*-
from sys import argv
from my_function import weather, torgi_resurs, minfin, coin, holiday
from my_class import facebook, telegram, twitter

fb = facebook.Facebook()
tg = telegram.Telegram()
tw = twitter.Twitter()

if argv[1] == "startDay":
    fb.picture_facebook('newDay.png', "StartDay")
elif argv[1] == "WVCF":
    weather = weather.ReadWather().water_read(how='today')
    valuta = torgi_resurs.return_valuta()
    coin = coin.coin_now()
    fuel = minfin.fuel()

    fb.text_facebook(fuel, "WVCF.flue()")
    tg.text_telegram(fuel, "WVCF.flue()")
    tw.text_twiter(fuel, "WVCF.flue()")

    fb.text_facebook(coin, "WVCF.coin()")
    tg.text_telegram(coin, "WVCF.coin()")
    tw.text_twiter(coin, "WVCF.coin()")

    fb.text_facebook(valuta, "WVCF.valuta()")
    tg.text_telegram(valuta, "WVCF.valuta()")
    tw.text_twiter(valuta, "WVCF.valuta()")

    fb.text_facebook(weather, "WVCF.weather()")
    tg.text_telegram(weather, "WVCF.weather()")
    tw.text_twiter(weather, "WVCF.weather()")
elif argv[1] == "weatherToday":
    weather = weather.ReadWather().water_read(how='today')
    tg.text_telegram(weather, "weatherToday")
    fb.text_facebook(weather, "weatherToday")
    tw.text_twiter(weather, "weatherToday")
elif argv[1] == "weatherNow":
    weather = weather.ReadWather().water_read(how='now')
    fb.text_picture_facebook(weather, 'shortPostWeather.png', "weatherNow")
    tg.text_telegram(weather, "weatherNow")
    tw.text_twiter(weather, "weatherNow")
elif argv[1] == "weatherTomorrow":
    weather = weather.ReadWather().water_read(how='tomorrow')
    fb.text_facebook(weather, "weatherTomorrow")
    tg.text_telegram(weather, "weatherTomorrow")
    tw.text_twiter(weather, "weatherTomorrow")
elif argv[1] == "valuta":
    valuta = torgi_resurs.return_valuta()
    fb.text_facebook(valuta, "valuta")
    tg.text_telegram(valuta, "valuta")
    tw.text_twiter(valuta, "valuta")
elif argv[1] == "coin":
    coin = coin.coin_now()
    fb.text_facebook(coin, "coin")
    tg.text_telegram(coin, "coin")
    tw.text_twiter(coin, "coin")
elif argv[1] == "fuel":
    fuel = minfin.fuel()
    fb.text_facebook(fuel, "fuel")
    tg.text_telegram(fuel, "fuel")
    tw.text_twiter(fuel, "fuel")
elif argv[1] == "holidayNow":
    holiday = holiday.holiday()
    if holiday:
        fb.text_facebook(holiday, "holidayNow")
        tg.text_telegram(holiday, "holidayNow")
        tw.text_twiter(holiday, "holidayNow")
elif argv[1] == "holidayPre":
    holiday = holiday.holiday_pre_one()
    if holiday:
        fb.text_facebook(holiday, "holidayPre")
        tg.text_telegram(holiday, "holidayPre")
        tw.text_twiter(holiday, "holidayPre")

