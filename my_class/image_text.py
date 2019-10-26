# -*- coding: utf-8 -*-
import config
from my_class import report, language
from PIL import Image, ImageDraw, ImageFont, ImageFilter


class TextToImage:
    _translator = language.Language()
    _report = report.Report()

    @staticmethod
    def font_image(font_name, font_size):
        return ImageFont.truetype(config.ANTHILL_FONTS_PATH + font_name + '.ttf', font_size)

    @staticmethod
    def to_image(image_path_in_images, image_name, image_format, text, image_font, x_position, y_position,
                 save_image_format):
        path = config.ANTHILL_IMAGES_PATH + image_path_in_images + '/'
        image = Image.open(path + image_name + '.' + image_format.lower())
        # из png в jpg выравнивание цветов
        if image.mode == 'RGBA' and save_image_format.lower() != 'png':
            image = image.convert("RGB")
        draw = ImageDraw.Draw(image)
        draw.text((x_position, y_position), text, (255, 184, 44), font=image_font)

        # если присутствует префикс _text у картинки ничего не вставляем
        if '_text' in image_name:
            pre = ''
        else:
            pre = config.ANTHILL_IMAGES_PRE_NAME_OUT

        save_image = path + image_name + pre + '.' + save_image_format.lower()
        image.save(save_image)
        return save_image

    def set_text_to_image(self, image_path_in_images, image_name, image_format, text, font_name, font_size, x_position,
                          y_position, save_image_format):
        try:
            save_image = self.to_image(image_path_in_images, image_name, image_format, text,
                                       self.font_image(font_name, font_size), x_position, y_position, save_image_format)
            self._report.set_report(__name__,
                                    self._translator.get_shifting('text_in_picture') + ' >> ' + save_image)
        except Exception as e:
            self._report.set_report_error(__name__,
                                          self._translator.get_shifting('error_text_in_picture') + ' >> ' + str(e))
