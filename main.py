import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import telebot
from telebot import types
import keyboard

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Нажмите на кнопку 'Short или Long', чтобы начать.", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Short":
        bot.send_message(message.chat.id, "Давайте зададим параметры. Нажмите Short еще раз для подтверждения")
        bot.register_next_step_handler(message, ask_parameters)
    elif message.text == "Long":
        bot.send_message(message.chat.id, "Давайте зададим параметры. Нажмите Long еще раз для подтверждения")
        bot.register_next_step_handler(message, ask_parameters2)


def ask_parameters(message):
    bot.send_message(message.chat.id, "Введите Айди:")
    bot.register_next_step_handler(message, ask_roi)

def ask_roi(message):
    global text_content
    text_content = message.text
    bot.send_message(message.chat.id, "Введите ROI:")
    bot.register_next_step_handler(message, ask_entry_price)

def ask_entry_price(message):
    global text_content2
    text_content2 = message.text
    bot.send_message(message.chat.id, "Введите цену входа:")
    bot.register_next_step_handler(message, ask_current_price)

def ask_current_price(message):
    global text_content3
    text_content3 = message.text
    bot.send_message(message.chat.id, "Введите текущую цену:")
    bot.register_next_step_handler(message, send_image_with_text)

def send_image_with_text(message):
    global text_content4
    text_content4 = message.text

    img = cv2.imread('short.jpeg')
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_path = "Felbridge.ttf."
    font_path2 = "InnovaAlt-Demi.ttf"

    font_size1, thickness1 = 55, 5
    font_size2, thickness2 = 100, 10
    font_size3, thickness3 = 40, 2
    font_size4, thickness4 = 40, 2

    font1 = ImageFont.truetype(font_path, font_size1)
    font2 = ImageFont.truetype(font_path2, font_size2)
    font3 = ImageFont.truetype(font_path2, font_size3)
    font4 = ImageFont.truetype(font_path2, font_size4)

    draw.text((55, 235), text_content, font=font1, fill=(255, 255, 255))
    draw.text((55, 415), text_content2, font=font2, fill=(44, 174, 104, 255))
    draw.text((55, 610), text_content3, font=font3, fill=(255, 255, 255))
    draw.text((55, 750), text_content4, font=font4, fill=(255, 255, 255))

    img_with_text = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('short_2.jpg', img_with_text)

    with open('short_2.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


def ask_parameters2(message):
    bot.send_message(message.chat.id, "Введите Айди:")
    bot.register_next_step_handler(message, ask_roi2)

def ask_roi2(message):
    global text_content
    text_content = message.text
    bot.send_message(message.chat.id, "Введите ROI:")
    bot.register_next_step_handler(message, ask_entry_price2)

def ask_entry_price2(message):
    global text_content2
    text_content2 = message.text
    bot.send_message(message.chat.id, "Введите цену входа:")
    bot.register_next_step_handler(message, ask_current_price2)

def ask_current_price2(message):
    global text_content3
    text_content3 = message.text
    bot.send_message(message.chat.id, "Введите текущую цену:")
    bot.register_next_step_handler(message, send_image_with_text2)

def send_image_with_text2(message):
    global text_content4
    text_content4 = message.text

    img = cv2.imread('long.jpeg')
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_path = "Felbridge.ttf."
    font_path2 = "InnovaAlt-Demi.ttf"

    font_size1, thickness1 = 55, 5
    font_size2, thickness2 = 100, 10
    font_size3, thickness3 = 40, 2
    font_size4, thickness4 = 40, 2

    font1 = ImageFont.truetype(font_path, font_size1)
    font2 = ImageFont.truetype(font_path2, font_size2)
    font3 = ImageFont.truetype(font_path2, font_size3)
    font4 = ImageFont.truetype(font_path2, font_size4)

    draw.text((55, 235), text_content, font=font1, fill=(255, 255, 255))
    draw.text((55, 415), text_content2, font=font2, fill=(44, 174, 104, 255))
    draw.text((55, 610), text_content3, font=font3, fill=(255, 255, 255))
    draw.text((55, 750), text_content4, font=font4, fill=(255, 255, 255))

    img_with_text = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('long_2.jpg', img_with_text)

    # отправляем изображение с текстом пользователю
    with open('long_2.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton(text="Short"), types.KeyboardButton(text="Long"))

# Запуск бота
bot.polling()
