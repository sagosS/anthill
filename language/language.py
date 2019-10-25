def language_result(lang_query):
    if lang_query == 'ru':
        return dict(
            site_is_loaded='сайт успешно загружен',
            something_went_wrong='что-то пошло не так, проверте правильность вводa',
            not_possible_process='данный запрос не возможно обработать прямо сейчас, попробуйте позже',
            text_in_picture='текст вставлен в кртинку',
            error_text_in_picture='текст невставлен в кртинку',
            facebook_post='пост опубликован на facebook',
            facebook_post_error='ошибка публикации на facebook',
            facebook_picture='картинка опубликована на facebook',
            facebook_picture_error='ошибка публикации картинки на facebook',
            facebook_post_picture='опубликован пост и картинка на facebook',
            facebook_post_picture_error='ошибка публикации поста и картинки на facebook',
            db_execute_ok='успешное получение запроса из БД',
            db_execute_error='ошибка получениея запроса к БД',
            db_execute_commit_ok='запрос к БД сформирован',
            db_execute_commit_error='ошибка формирования запроса к БД',
            db_commit_ok='успешное обращение к БД',
            db_commit_error='ошибка обращения к БД',
            telegram_post='пост опубликован на telegram',
            telegram_post_error='ошибка публикации на telegram'
        )
