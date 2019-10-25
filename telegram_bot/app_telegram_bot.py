from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

api = '883009969:AAE9PTeYk1lHTZ4U8fGoTXYE586wTAaXlBk'
updater = Updater(token=api, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher.bot.send_message(chat_id=-1001404262415, text='OK')


# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
#
#
# # /start
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)
#
#
# def hello(update, context):
#     update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
#
#
# updater.dispatcher.add_handler(CommandHandler('hello', hello))
#
#
# def handle_message(bot, update):
#     print("Received", bot.effective_message.text)
#     print(bot.effective_chat.__dict__)
#
#
# handler = MessageHandler(Filters.text | Filters.command, handle_message)
# updater.dispatcher.add_handler(handler)  # ставим обработчик всех текстовы
#
#
# def unknown(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=" Извините, я не понял эту команду. ")
#
#
# # Этот обработчик должен быть добавлен последним. Если вы добавите его
# # Некоторые сбитые с толку пользователи могут попытаться отправить команды боту, который он не понимает,
# # поэтому вы можете использовать фильтр MessageHandler
# # /unknown
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)
#
# updater.start_polling()
# updater.idle()
