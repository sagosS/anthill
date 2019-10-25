import facebook
import config
from my_class import language, report


class Facebook:
    _translator = language.Language()
    _report = report.Report()
    _api = config.ANTHILL_FACEBOOK_API
    _img_path = config.ANTHILL_IMAGES_PATH

    def __init__(self):
        self._graph = facebook.GraphAPI(access_token=self._api)

    def text_facebook(self, message, who_posted):
        try:
            self._graph.put_object(parent_object='me', connection_name='feed', message=message)
            self._report.set_report(__name__, self._translator.get_shifting('facebook_post') + ' >> ' + who_posted)
        except Exception as e:
            self._report.set_report_error(__name__, self._translator.get_shifting('facebook_post_error') + ' >> ' + str(e))

    def picture_facebook(self, image, who_posted):
        try:
            self._graph.put_photo(image=open(self._img_path + image, 'rb'))
            self._report.set_report(__name__, self._translator.get_shifting('facebook_picture') + ' >> ' + who_posted)
        except Exception as e:
            self._report.set_report_error(__name__,
                                          self._translator.get_shifting('facebook_picture_error') + ' >> ' + str(e))

    def text_picture_facebook(self, message, image, who_posted):
        try:
            self._graph.put_photo(image=open(self._img_path + image, 'rb'), message=message)
            self._report.set_report(__name__,
                                    self._translator.get_shifting('facebook_post_picture') + ' >> ' + who_posted)
        except Exception as e:
            self._report.set_report_error(__name__,
                                          self._translator.get_shifting('facebook_post_picture_error') + ' >> ' + str(e))
