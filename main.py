import json
from func_lists import *

TOKEN = "6182241691:AAFl3lahEdNLQGp3hurvMI8JeYbAIRlHc54"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет, ты попал на квест "Бой с Минотавром", желаешь начать?', reply_markup=start)
    file = open("user_data.json", "w")
    full[str(message.from_user.id)] = {}
    full[str(message.from_user.id)]['number_question'] = "1"
    full[str(message.from_user.id)]['armor'] = False
    full[str(message.from_user.id)]['kemper'] = False
    full[str(message.from_user.id)]['dye_in_pvp'] = False
    full[str(message.from_user.id)]['niceable'] = False
    json.dump(full, file)
    file.close()


@bot.message_handler(commands=['number'])
def numb(message):
    if full[str(message.from_user.id)]['number_question'] == "1":
        bot.send_message(message.chat.id, 'Отлично!')
        bot.send_message(message.chat.id, fulltexts["010"])
        bot.send_message(message.chat.id, fulltexts["011"], reply_markup=napravlenie)
        full[str(message.from_user.id)]['number_question'] = "2"
    elif full[str(message.from_user.id)]['number_question'] == "2":
        bot.send_message(message.chat.id, fulltexts["010"])
        bot.send_message(message.chat.id, fulltexts["011"], reply_markup=napravlenie)
    elif full[str(message.from_user.id)]['number_question'] == "3":
        if full[str(message.from_user.id)]['vetka'] == "0":
            bot.send_message(message.chat.id, fulltexts["220"])
            bot.send_message(message.chat.id, fulltexts["230"], reply_markup=minotavr)
        if full[str(message.from_user.id)]['vetka'] == "1":
            bot.send_message(message.chat.id, fulltexts["120"])
            bot.send_message(message.chat.id, fulltexts["130"], reply_markup=tryapka)


@bot.message_handler(content_types=['text'])
def otvetka(message):
    def photo(link):
        with open(link, 'rb') as f:
            bot.send_photo(message.chat.id, f)
    try:
        file = open("user_data.json", "r")
        full = json.load(file)
        file = open("user_data.json", "w")
        if message.text == 'Да!' and full[str(message.from_user.id)]['number_question'] == "1":
            bot.send_message(message.chat.id, 'Отлично!')
            bot.send_message(message.chat.id, fulltexts["010"], photo('media/010.png'))
            bot.send_message(message.chat.id, fulltexts["011"], photo('media/011.png'), reply_markup=napravlenie)
            full[str(message.from_user.id)]['number_question'] = "2"
        elif full[str(message.from_user.id)]['number_question'] == "2":
            if message.text == 'Налево':
                full[str(message.from_user.id)]['vetka'] = "1"
                full[str(message.from_user.id)]['number_question'] = "3"
                bot.send_message(message.chat.id, fulltexts["120"],  photo('media/120.png'))
                bot.send_message(message.chat.id, fulltexts["130"], photo('media/130.png'), reply_markup=tryapka)
            elif message.text == 'Направо':
                full[str(message.from_user.id)]['vetka'] = "0"
                full[str(message.from_user.id)]['number_question'] = "3"
                bot.send_message(message.chat.id, fulltexts["220"], photo('media/220.png'))
                bot.send_message(message.chat.id, fulltexts["230"], photo('media/230.png'), reply_markup=minotavr)
        elif full[str(message.from_user.id)]['number_question'] == "3":
            if full[str(message.from_user.id)]['vetka'] == "1":
                if message.text == 'Вытереть подошву тряпкой.':
                    bot.send_message(message.chat.id, fulltexts["131"], photo('media/131.png'), reply_markup=end)
                    bot.send_message(message.chat.id, fulltexts["131.5"], photo('media/131.5.png'))
                    full[str(message.from_user.id)]['number_question'] = ""
                if message.text == 'Пойти дальше не обращая внимание.':
                    bot.send_message(message.chat.id, fulltexts["132"], photo('media/132.png'), reply_markup=end)
                    bot.send_message(message.chat.id, fulltexts["132.5"], photo('media/132.5.png'))
                    full[str(message.from_user.id)]['number_question'] = ""
            if full[str(message.from_user.id)]['vetka'] == "0":
                if message.text == 'Попытаться проскочить.':
                    bot.send_message(message.chat.id, fulltexts["231"], photo('media/231.png'))
                    bot.send_message(message.chat.id, fulltexts["231.5"], photo('media/231.5.png'), reply_markup=end)
                    bot.send_message(message.chat.id, fulltexts["23"], photo('media/23.png'))
                    full[str(message.from_user.id)]['number_question'] = ""
                if message.text == 'Попытаться тихонько пройти мимо.':
                    bot.send_message(message.chat.id, fulltexts["232"], photo('media/232.png'), reply_markup=end)
                    bot.send_message(message.chat.id, fulltexts["23"], photo('media/23.png'))
                    full[str(message.from_user.id)]['number_question'] = ""
        else:
            bot.send_message(message.chat.id, 'Ты видимо ошибся, нажми /start для перепрохождения или /number, чтобы узнать текущий вопрос.')
        json.dump(full, file)
        file.close()
    except:
        bot.send_message(message.chat.id, 'Для начала нажми /start.')


bot.polling()





