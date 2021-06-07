
import telebot
apiKey='1667737815:AAFcJZNJnS-VbXCouAe6ZmcLX6XCVizdCQc'

bot=telebot.TeleBot(apiKey)
@bot.message_handler(commands=['hi','hai','Hi','Hai','HI','HAI'])
def hi(msg):
    bot.send_message(msg.chat.id,'hloo')
    print(msg.chat.id)
bot.polling()