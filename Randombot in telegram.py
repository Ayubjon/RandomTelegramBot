import telebot
import random

from telebot import types

Token = ""  #Write the token of your bot

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    #greeting
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("🎲Write interval")
    item2 = types.KeyboardButton("😁just speak")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Hi, {0.first_name}! My name is <b>{1.first_name}</b>. I am a bot that was written for printing the random number in interval that you will write".format(message.from_user, bot.get_me()),
        parse_mode = 'HTML', reply_markup = markup)


a = [0]


@bot.message_handler(content_types=['text'])
def speak(message):
    #bot.send_message(message.chat.id, message.text)
    if message.chat.type == 'private':
        if message.text == "🎲Write interval":
            bot.send_message(message.chat.id, "Write the interval like a (number1-number2), example:\n1-50")
            a[0] = 0
        elif message.text == "😁just speak":
            bot.send_message(message.chat.id, "let's speak")
            a[0] = 1
        else:
            if a[0] == 1:
                bot.send_message(message.chat.id, message.text)
                return
            # Checking is written message right
            check = 0; check1 = 0; check2 = 0
            for i in message.text:
                if (i >= '0' and i <= '9' and check == 0):
                    check1 += 1
                    continue
                elif (i >= '0' and i <= '9' and check):
                    check2 += 1
                elif i == '-': check += 1
                else:
                    bot.send_message(message.chat.id, "Write the interval like a (number-number), example:\n1-50")
                    return
            if check != 1 or check1 == 0 or check2 == 0:
                bot.send_message(message.chat.id, "Write the interval like a (number-number), example:\n1-50")
                return
            # gets numbers
            d, e = map(int, message.text.split('-'))
            # Printing random number
            if d <= e: bot.send_message(message.chat.id, random.randint(d, e))
            else : bot.send_message(message.chat.id, "number1-number2 should be:\nnumber1 <= number2")


# RUN
bot.polling(none_stop = True)
