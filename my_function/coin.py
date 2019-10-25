import json
import time
import urllib.request
import datetime

today = datetime.datetime.today()
t_day = int(today.strftime("%d"))-1
old_date = today.strftime(str(t_day)+".%m.%Y")

url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,XRP,BCH&tsyms=USD,BTC,ETH,XRP,BCH'"
url_usd = "https://api.privatbank.ua/p24api/exchange_rates?json&date={}".format(old_date)

def coin_start():
    return (json.load(urllib.request.urlopen(url)))["BTC"]["USD"]

def ethereum_start():
    return (json.load(urllib.request.urlopen(url)))["ETH"]["USD"]

def ripple_start():
    return (json.load(urllib.request.urlopen(url)))["XRP"]["USD"]

def bitcoin_cash_start():
    return (json.load(urllib.request.urlopen(url)))["BCH"]["USD"]

def usd_req():
        
    result = float("{:.2f}".format(json.load(urllib.request.urlopen(url_usd))['exchangeRate'][16]['saleRateNB']))
    return result

coin_start = coin_start()
ethereum_start = ethereum_start()
ripple_start = ripple_start()
bitcoin_cash_start = bitcoin_cash_start()
usd_req = usd_req()

def coin_now():

    return (
        f'🔰Курс криптовалют\n'
        f'▪Bitcoin: {coin_start}$ >>> {float("{:.1f}".format(coin_start*usd_req))}грн.\n'
        f'▪BitcCash: {bitcoin_cash_start}$ >>> {float("{:.1f}".format(bitcoin_cash_start*usd_req))}грн.\n'
        f'▪Ethereum: {ethereum_start}$ >>> {float("{:.1f}".format(ethereum_start*usd_req))}грн.\n'
        f'▪Ripple: {ripple_start}$ >>> {float("{:.1f}".format(ripple_start*usd_req))}грн.\n'
        )