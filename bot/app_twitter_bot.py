#   * Автор: Сердюк Николай Валериевич.
#   * Компания: KrSoup.
#   * e-mail: uainfo777@gmail.com.
#   * Разработка: "Криворожский Суп".
#   * Все права защищены международным законодательством.
#   * Копиревание или публикация без согласия автора запрещены.
import os
import tweepy
import config
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError


def init_auth(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def download_image(url):
    try:
        file_path = os.path.abspath(os.path.split(url)[-1])
        urlretrieve(url, file_path)
    except IndexError as e:
        print(e)
        file_path = None
    except HTTPError as e:
        print(e)
        file_path = None
    return file_path


def send_tweet_with_media(api, text, image):
    if 'http://' not in image:
        assert os.path.isfile(image)
        file_path = image
    else:
        # качаем файл из сети
        file_path = download_image(image)

    assert file_path is not None, "Not found image (for twitter)"
    api.update_with_media(file_path, text)


def send_tweet(api, text):
    api.update_status(text)


twitter_text = 'OK'
image = 'https://pp.vk.me/c624516/v624516517/31b6b/6kViWNZI6n4.jpg'
twitter_api = init_auth(config.ANTHIL_TWITTER_CONSUMER, config.ANTHIL_TWITTER_CONSUMER_SECRET,
                        config.ANTHIL_TWITTER_TOKEN, config.ANTHIL_TWITTER_TOKEN_SECRET)
send_tweet(twitter_api, twitter_text)
