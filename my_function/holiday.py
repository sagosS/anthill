import datetime
from my_class import dbhelper

db = dbhelper.DBHelper()
today = datetime.datetime.today()
day = today.strftime("%d")
month = today.strftime("%m")


# todo: праздников бывает несколько разобратся с запросами к БД

def holiday():
    result_db = db.holiday_check(this_date())
    if result_db:
        return f'Сегодня празднуют "{result_db[2]}"\n\n{result_db[3]}'
    else:
        return False


def holiday_pre_one():
    result_db = db.holiday_check(this_date(1) + '.' + month)
    if result_db:
        return f'Завтра празднуют "{result_db[2]}"'
    else:
        return holiday_day_two()


def holiday_day_two():
    result_db = db.holiday_check(this_date(2) + '.' + month)
    if result_db:
        return f'После завтра празднуют "{result_db[2]}"'
    else:
        return False


def this_date(pre=0):
    now_day = today.strftime("%d")
    now_month = today.strftime("%m")
    if pre:
        date = str(int(now_day) + pre)
    else:
        date = now_day + '.' + now_month
    return date
