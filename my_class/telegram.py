from telegram.ext import Updater
import config
from my_class import language, report


class Telegram:
    _translator = language.Language()
    _report = report.Report()
    _api = config.ANTHILL_TELEGRAM_API
    _chat_id = config.ANTHILL_TELEGRAM_CHAT_ID

    def __init__(self):
        updater = Updater(token=self._api, use_context=True)
        self._dispatcher = updater.dispatcher

    def text_telegram(self, message, who_posted):
        try:
            self._dispatcher.bot.send_message(chat_id=self._chat_id, text=message)
            self._report.set_report(__name__, self._translator.get_shifting('telegram_post') + ' >> ' + who_posted)
        except Exception as e:
            self._report.set_report_error(__name__, self._translator.get_shifting('telegram_post_error') + ' >> ' + str(e))
