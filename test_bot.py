 
import telebot
import ScrapingMisisSchelude
token = '1871012202:AAEZKeB1AGmYNty2n5jwftN_yRAMe0kCEfA'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
  
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'расписание':
        #bot.send_message(message.from_user.id, 'Ща')
        today,current_time = ScrapingMisisSchelude.date()
        schelude = ScrapingMisisSchelude.parsing_lesson('304',current_time,today)
        bot.send_message(message.from_user.id,  schelude)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
if __name__ == '__main__':
     bot.polling(none_stop=True)