import urllib.request

usd_i = 1
eur_i = 2

url = urllib.request.urlopen("https://www.ueex.com.ua/informer_ugd.js?lang=rus&n=3&encoding=utf&&width=300").read()


def torgi_query(query):
    list_req = str(url.decode('utf-8')).split(");")

    usd2 = list_req[7]
    eur2 = list_req[8]

    a95a = list_req[10]
    a95p = list_req[11]

    a92a = list_req[12]
    a92p = list_req[13]

    disela = list_req[14]
    diselp = list_req[15]

    lpg_t = list_req[16]
    lpg_u = list_req[17]
    lpg_b = list_req[18]
    lpg_y = list_req[19]
    lpg_s = list_req[20]

    if query == 'valuta':
        return [usd2, eur2]
    elif query == 'toplivo':
        return [a92a, a92p, a95a, a95p, disela, diselp]
    elif query == 'lpg':
        return [lpg_t, lpg_u, lpg_b, lpg_y, lpg_s]
    elif query == 'all':
        return [usd2, eur2, a95a, a95p, a92a, a92p, disela, diselp, lpg_t, lpg_u, lpg_b, lpg_y, lpg_s]


def ink_val(str_v, i, col, dec):
    val = (str(str_v).split('<span>')[i][:col]).replace(" ", "").replace(",", ".")
    return "{:.2f}".format(float(val) / dec)


def return_valuta():
    resulr = torgi_query('valuta')
    return f"🧐Котировка валют:\n" \
        f"▪USD: {ink_val(resulr[0], 1, 8, 100)}грн.\n" \
        f"▪EUR: {ink_val(resulr[1], 1, 8, 100)}грн."


def return_toplivo():
    resulr = torgi_query('toplivo')
    return f"Торги топливо:\n\n" \
        f"а92\t\t\t\t\t\t(а):\t\t\t{ink_val(resulr[0], 1, 8, 1000)}грн.\n" \
        f"а92\t\t\t\t\t\t(ж):\t\t{ink_val(resulr[1], 1, 8, 1000)}грн.\n"\
        f"а95\t\t\t\t\t\t(а):\t\t\t{ink_val(resulr[2], 1, 8, 1000)}грн.\n" \
        f"а95\t\t\t\t\t\t(ж):\t\t{ink_val(resulr[3], 1, 8, 1000)}грн.\n"\
        f"DISEL\t\t(а):\t\t\t{ink_val(resulr[4], 1, 8, 1000)}грн.\n" \
        f"DISEL\t\t(ж):\t\t{ink_val(resulr[5], 1, 8, 1000)}грн.\n\n" \
        f"a - доставка авто путём\n" \
        f"ж - доставка ж/д путём"


def return_lpg():
    resulr = torgi_query('lpg')
    return f"Газ для заправок Украины:\n\n" \
        f"Тимофеевская:\t\t{ink_val(resulr[0], 1, 8, 1000)}грн.\n" \
        f"Юльчевский:\t\t\t\t{ink_val(resulr[1], 1, 8, 1000)}грн.\n" \
        f"Базилевщина:\t\t\t{ink_val(resulr[2], 1, 8, 1000)}грн.\n" \
        f"Яблоновское:\t\t\t{ink_val(resulr[3], 1, 8, 1000)}грн.\n" \
        f"Шебелинское:\t\t{ink_val(resulr[4], 1, 8, 1000)}грн."


def info_gas():
    info_str = \
        '"Т" \n Тимофеевская УУВУ ГПУ\n "Прлтавгаздобыча"\n\n' \
        '"Ю" \n Юльчевский ЦПДКГ ГПУ\n "Шебелинкагаздобыча"\n\n' \
        '"Б" \n ТЦСК "Базилевщина" УП\n\n' \
        '"Я" \n Яблоновское ОП\n Управление по переработке\n\n' \
        '"Ш" \n ОПГКН Шебелинское УП'

    return info_str
