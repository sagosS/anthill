from my_class import image_text

text_img = image_text.TextToImage()


# 17 > 120 px max
# 43 > 45 px max


def text_holiday(print_text, position):
    result = dict()
    result['margin_left'] = 20
    result['print_text'] = print_text
    col_literal = len(print_text)
    if position == 'title':
        result['font_size'] = 43
        result['margin_bottom'] = 463
    elif position == 'text':
        if col_literal >= 17:
            weight = 1200 - (result['margin_left'] * 2)
            result['font_size'] = int(round((weight / col_literal) * 1.65))
        else:
            result['font_size'] = 120
        result['margin_bottom'] = (630 - result['font_size']) - ((140 - result['font_size']) / 2)
    else:
        result = False

    return result


title = text_holiday('С праздником суповары', 'title')
text = text_holiday('Всемирный день защиты морских', 'text')
# 'Всемирный день защиты морских млекопитающих'

text_img.set_text_to_image('holidays', 'blank', 'png', title['print_text'], 'Ubuntu-Light',
                           title['font_size'], title['margin_left'], title['margin_bottom'], 'jpg')
text_img.set_text_to_image('holidays', 'blank_text', 'jpg', text['print_text'], 'Ubuntu-Bold',
                           text['font_size'], text['margin_left'], text['margin_bottom'], 'jpg')
