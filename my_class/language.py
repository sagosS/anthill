import config
from language.language import language_result


class Language:
    language: str
    lang_dict: dict

    def __init__(self):
        self.language = config.ANTHILL_LANGUAGE
        self.lang_dict = language_result(self.language)

    def get_shifting(self, lang_query):
        # TODO: реализовть чтение с файл txt
        result = self.lang_dict[lang_query]
        return result
