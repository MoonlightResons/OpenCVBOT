import telebot
from telebot import types


main = telebot.types.ReplyKeyboardMarkup(True)
main.row('Short', "Long")
