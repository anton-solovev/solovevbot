 
import telebot
bot = telebot.TeleBot('1871012202:AAEZKeB1AGmYNty2n5jwftN_yRAMe0kCEfA')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
bot.polling(none_stop=True)