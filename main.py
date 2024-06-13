import telebot
from telebot import types
from about import about_text
from config import token_bot
from database import get_all_servicii, add_serviciu
from generate_car_list import generate_car_list, generate_pagination_markup

bot = telebot.TeleBot(token_bot)
waiting_for_serviciu = {}


@bot.message_handler(commands=['start', 'help', 'stop'])
def command_handler(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Despre Noi')
        btn2 = types.KeyboardButton('Termeni și Condiții')
        btn3 = types.KeyboardButton('Servicii Prestate')
        btn4 = types.KeyboardButton('Flota de Mașini')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Bine ai venit la Supreme Rentals! Alege o opțiune:", reply_markup=markup)
    elif message.text == '/help':
        bot.send_message(message.chat.id, "Lista de comenzi disponibile:\n"
                                          "/start sau /menu - Pentru afișarea meniului principal\n"
                                          "/help - Afișează această listă de comenzi\n"
                                          "/stop - Pentru oprirea botului")
    elif message.text == '/stop':
        bot.send_message(message.chat.id, "Botul a fost oprit.")
        bot.stop_polling()
    else:
        bot.send_message(message.chat.id, 'Scuze, nu înțeleg această comandă.')

# alta modalitate de a adauga un serveciul: /add serviciu!.

# @bot.message_handler(commands=['add'])
# def handle_add(message):
#     if len(message.text.split(maxsplit=1)) > 1:
#         serviciu = message.text.split(maxsplit=1)[1]
#         add_serviciu(serviciu)
#         bot.reply_to(message, f"Serviciu {serviciu} adăugat.")
#     else:
#         bot.reply_to(message, "Te rog să introduci un serviciu după comanda /add, exemplu: '/add serviciul prestat!'")


@bot.message_handler(commands=['add'])
def handle_add(message):
    chat_id = message.chat.id
    waiting_for_serviciu[chat_id] = True
    bot.send_message(chat_id, "Te rog să introduci numele serviciului pe care vrei să-l adaugi.")


@bot.message_handler(func=lambda message: message.chat.id in waiting_for_serviciu)
def handle_serviciu(message):
    chat_id = message.chat.id
    serviciu = message.text.strip()
    if serviciu:
        add_serviciu(serviciu)
        bot.send_message(chat_id, f"Serviciu {serviciu} adăugat.")
    else:
        bot.send_message(chat_id, "Te rog să introduci un nume valid pentru serviciu.")
    del waiting_for_serviciu[chat_id]


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == 'Despre Noi':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Despre Noi", url="https://supremerentals.md/about")
        markup.add(btn)
        bot.send_message(message.chat.id, about_text, parse_mode="HTML", reply_markup=markup)
    elif message.text == 'Termeni și Condiții':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Termeni și Condiții", url="https://supremerentals.md/conditii")
        markup.add(btn)
        bot.send_message(message.chat.id, 'Apasă pe butonul de mai jos pentru a deschide pagina Termeni și Condiții:',
                         reply_markup=markup)
    elif message.text == 'Servicii Prestate':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("Află mai multe", callback_data="servicii")
        markup.add(btn)
        bot.send_message(message.chat.id,
                         'Apasă pe butonul de mai jos pentru a afla mai multe despre serviciile prestate:',
                         reply_markup=markup)
    elif message.text == 'Flota de Mașini':
        start, end = 0, 5
        car_list_messages = generate_car_list(start, end)
        pagination_markup = generate_pagination_markup(start, end)
        for car_message, car_image in car_list_messages:
            bot.send_photo(message.chat.id, car_image, caption=car_message)
        bot.send_message(message.chat.id, "Navigare:", reply_markup=pagination_markup)
    else:
        bot.send_message(message.chat.id, 'Scuze, nu înțeleg această comandă.')


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data.startswith("prev_") or call.data.startswith("next_"):
        _, start, end = call.data.split('_')
        start, end = int(start), int(end)
        car_list_messages = generate_car_list(start, end)
        pagination_markup = generate_pagination_markup(start, end)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Flota de Mașini:")
        for car_message, car_image in car_list_messages:
            bot.send_photo(call.message.chat.id, car_image, caption=car_message)
        bot.send_message(call.message.chat.id, "Navigare:", reply_markup=pagination_markup)
    elif call.data == "servicii":
        servicii = get_all_servicii()
        if servicii:
            response = "<b>\u2728 Serviciile prestate \u2728</b>\n\n" + "\n".join(
                [f"-  {servici[1]}" for servici in servicii])
        else:
            response = "Nu s-au găsit servicii."
        bot.send_message(call.message.chat.id, response, parse_mode="HTML")


bot.polling(none_stop=True)
