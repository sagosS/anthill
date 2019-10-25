import sqlite3
import config
from my_class import report, language


class DBHelper:
    _translator = language.Language()
    _report = report.Report()
    _db_name = config.ANTHILL_DB_PATH + config.ANTHILL_DB_NAME + config.ANTHILL_DB_PREF
    _install_db_table = '''CREATE TABLE IF NOT EXISTS holidays (
               id integer primary key AUTOINCREMENT,
               date_holidays text,
               name_holidays text,
               text_holidays text,
               image_holidays text,
               show_holidays integer default 1
               )'''

    def __init__(self):
        self.conn = sqlite3.connect(self._db_name, check_same_thread=False)

    # создание баз данных
    def setup(self):
        self.commit_database(self._install_db_table)

    # получение записи из DB
    def arguments_in_db(self, stmt, args):
        try:
            result = self.conn.execute(stmt, args)
            self._report.set_report(__name__, self._translator.get_shifting(
                'db_execute_ok') + ' >> ' + 'query=' + stmt + 'args=' + str(args))
            return result.fetchone()
        except Exception as e:
            self._report.set_report_error(__name__, self._translator.get_shifting(
                'db_execute_error') + ' >> ' + 'query=' + stmt + 'args=' + str(args) + ' >> ' + str(e))

    # обращение к DB
    def commit_database(self, stmt, args=()):
        try:
            self.conn.execute(stmt, args)
            self._report.set_report(__name__, self._translator.get_shifting(
                'db_execute_commit_ok') + ' >> ' + 'query=' + stmt + 'args=' + str(args))
        except Exception as e:
            self._report.set_report_error(__name__, self._translator.get_shifting(
                'db_execute_commit_error') + ' >> ' + 'query=' + stmt + 'args=' + str(args) + ' >> ' + str(e))
        try:
            self.conn.commit()
            self._report.set_report(__name__, self._translator.get_shifting(
                'db_commit_ok') + ' >> ' + 'query=' + stmt + 'args=' + str(args))
        except Exception as e:
            self._report.set_report_error(__name__, self._translator.get_shifting(
                'db_commit_error') + ' >> ' + 'query=' + stmt + 'args=' + str(args) + ' >> ' + str(e))

    def holiday_check(self, date):
        stmt = "SELECT * FROM holidays WHERE date_holidays=(?)"
        args = (date,)
        result = self.arguments_in_db(stmt, args)
        return result

    # проверка записи раздников в DB если нет записывает
    def check_holidays_in_db(self, date_holidays, name_holidays, text_holidays, image_holidays):
        stmt = "SELECT name_holidays FROM holidays WHERE name_holidays=(?)"
        args = (name_holidays,)
        # если нет записи заносим
        if self.arguments_in_db(stmt, args) is None:
            print("++++++++++")
            self.set_holidays(date_holidays, name_holidays, text_holidays, image_holidays)

    def set_holidays(self, date_holidays, name_holidays, text_holidays, image_holidays):
        stmt = "INSERT INTO holidays VALUES (null,?,?,?,?,?)"
        args = (date_holidays, name_holidays, text_holidays, image_holidays, True)
        self.commit_database(stmt, args)

    # def set_holidays(self, user_id, lang):
    #     stmt = "UPDATE users SET lang_user = (?) WHERE user_id = (?)"
    #     args = (lang, user_id)
    #     self.conn.execute(stmt, args)
    #     self.conn.commit()

    # def delete_item(self, item_text):
    #     stmt = "DELETE FROM items WHERE description = (?)"
    #     args = (item_text,)
    #     self.conn.execute(stmt, args)
    #     self.conn.commit()
    #
    # def get_items(self):
    #     stmt = "SELECT description FROM items"
    #     return [x[0] for x in self.conn.execute(stmt)]
