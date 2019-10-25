import config as c
import datetime


class Report:
    _path = c.ANTHILL_REPORT_PATH + c.ANTHILL_REPORT_NAME + c.ANTHILL_REPORT_PREF
    _error_path = c.ANTHILL_REPORT_ERROR_PATH + c.ANTHILL_REPORT_ERROR_NAME + c.ANTHILL_REPORT_PREF

    @staticmethod
    def report_str(name_file, report, pre):
        today = datetime.datetime.today()
        if pre == 'set_report_error':
            pre = 'e'
        else:
            pre = 'i'
        return pre + ' ' + today.strftime("%Y-%m-%d %H.%M.%S") + ' >> ' + name_file + ' >> ' + report + '\n'

    @staticmethod
    def report(path, report_str):
        report = open(path, 'a')
        report.write(report_str)
        report.close()

    def set_report(self, name_file, report):
        report_str = self.report_str(name_file, report, self.set_report.__name__)
        self.report(self._path, report_str)
        return False

    def set_report_error(self, name_file, report):
        report_str = self.report_str(name_file, report, self.set_report_error.__name__)
        self.report(self._path, report_str)
        self.report(self._error_path, report_str)
        return False
