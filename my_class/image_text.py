# -*- coding: utf-8 -*-
import config
from my_class import report, language
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# TODO: проверка папки на существование и создание есди нет
# TODO: создание разных форматов из разных форматов png > jpg

class TextToImage:
    _translator = language.Language()
    _report = report.Report()

    @staticmethod
    def font_image(font_name, font_size):
        return ImageFont.truetype(config.ANTHILL_FONTS_PATH + font_name + '.ttf', font_size)

    @staticmethod
    def to_image(image_name, text, image_font, x_position, y_position, save_name_image):
        image = Image.open(config.ANTHILL_IMAGES_BLANK_PATH + image_name)
        draw = ImageDraw.Draw(image)
        draw.text((x_position, y_position), text, (255, 184, 44), font=image_font)
        image.save(config.ANTHILL_IMAGES_TEXT_PATH + save_name_image)
        return save_name_image

    def set_text_to_image(self, blank_image_name, text, font_name, font_size, x_position, y_position, save_name_image):
        try:
            save_name_image = self.to_image(blank_image_name, text, self.font_image(font_name, font_size), x_position,
                                            y_position, save_name_image)
            self._report.set_report(__name__,
                                    self._translator.get_shifting('text_in_picture') + ' >> ' + save_name_image)
        except Exception as e:
            self._report.set_report_error(__name__,
                                          self._translator.get_shifting('error_text_in_picture') + ' >> ' + str(e))
