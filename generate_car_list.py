from telebot import types
from car_list import car_fleet


def generate_car_list(start, end):
    messages = []
    for car in car_fleet[start:end]:
        car_message = car["name"]
        car_image = open(car["image"], 'rb')
        messages.append((car_message, car_image))
    return messages


def generate_pagination_markup(start, end):
    markup = types.InlineKeyboardMarkup()
    if start > 0:
        btn_prev = types.InlineKeyboardButton("Înapoi", callback_data=f"prev_{start-5}_{end-5}")
        markup.add(btn_prev)
    if end < len(car_fleet):
        btn_next = types.InlineKeyboardButton("Înainte", callback_data=f"next_{start+5}_{end+5}")
        markup.add(btn_next)
    btn_fleet = types.InlineKeyboardButton("Flota de Masini", url="https://supremerentals.md/")
    markup.add(btn_fleet)
    return markup