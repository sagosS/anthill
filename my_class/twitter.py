#   * Автор: Сердюк Николай Валериевич.
#   * Компания: KrSoup.
#   * e-mail: uainfo777@gmail.com.
#   * Разработка: "Криворожский Суп".
#   * Все права защищены международным законодательством.
#   * Копиревание или публикация без согласия автора запрещены.
import tweepy
import config
from my_class import language, report
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError


class Twitter:
    _translator = language.Language()
    _report = report.Report()
    _api = None
    _token = config.ANTHIL_TWITTER_TOKEN
    _token_secret = config.ANTHIL_TWITTER_TOKEN_SECRET
    _cons = config.ANTHIL_TWITTER_CONSUMER
    _cons_secret = config.ANTHIL_TWITTER_CONSUMER_SECRET
    _img_path = config.ANTHILL_IMAGES_PATH

    def __init__(self):
        auth = tweepy.OAuthHandler(self._cons, self._cons_secret)
        auth.set_access_token(self._token, self._token_secret)
        self._api = tweepy.API(auth)

    def text_picture_twiter(self, text, image):
        self._api.update_with_media(image, text)

    def text_twiter(self, text, who_posted):
        try:
            self._api.update_status(text)
            self._report.set_report(__name__, self._translator.get_shifting('twitter_post') + ' >> ' + who_posted)
        except Exception as e:
            self._report.set_report_error(__name__,
                                          self._translator.get_shifting('twitter_post_error') + ' >> ' + str(e))
