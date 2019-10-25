# -*- coding: utf-8 -*-
from my_class import report, language
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


class GetHTML:
    _translator = language.Language()
    _report = report.Report()

    def get_html(self, url):
        try:
            result = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
            self._report.set_report(__name__, self._translator.get_shifting('site_is_loaded') + ' >> ' + url)
        except HTTPError as e:
            result = self._report.set_report_error(__name__, self._translator.get_shifting(
                'something_went_wrong') + ' >> ' + url + ' >> ' + str(e))
        except URLError as e:
            result = self._report.set_report_error(__name__, self._translator.get_shifting(
                ['not_possible_process']) + ' >> ' + url + ' >> ' + str(e))

        return result
