import telebot
from telebot import types

bot = telebot.TeleBot("7917259019:AAHEgYhHQ-KXPcvDWc4gJAf19euGXRagGLM")


@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Лера, здарова")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Че как жизнь?", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):

    if message.text == "Лера, здарова":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True
        )  # создание новых кнопок
        btn1 = types.KeyboardButton("Как сделать план на день?")
        btn2 = types.KeyboardButton("Просмотреть очередь ожидания")
        btn3 = types.KeyboardButton("Календарь планирования тестирования")
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.from_user.id,
            "❓ Задайте интересующий вас вопрос",
            reply_markup=markup,
        )  # ответ бота

    elif message.text == "Как сделать план на день?":
        bot.send_message(
            message.from_user.id,
            "Ну это сложно... Попроси видос, мы про это проводили уже обучение",
            parse_mode="Markdown",
        )

    elif message.text == "Посмотреть очередь ожидания":
        bot.send_message(
            message.from_user.id,
            "Просмотреть очередь ожидания можно по "
            + "[ссылке](https://jira-medmis.bars.group/issues/?filter=14670)",
            parse_mode="Markdown",
        )

    elif message.text == "Календарь планирования тестирования":
        bot.send_message(
            message.from_user.id,
            "Календарь планирования тестирования смотри по "
            + "[ссылке](https://conf.bars.group/pages/viewpage.action?pageId=238701279)",
            parse_mode="Markdown",
        )


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
