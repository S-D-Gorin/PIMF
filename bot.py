import utils
import config
import telebot


BOT_TOKEN = config.BOT_TOKEN
GROUP_ID = config.GROUP_ID
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(content_types = ['text'])
def spam_security(message):
    
    if str(message.chat.id) in GROUP_ID\
        and str(message.from_user.username) not in config.SUPERUSERS:
    
    
        if not utils.Check.phone(message):
            bot.delete_message(message.chat.id, message.message_id)
            utils.send_info_message_and_delete_old_message(
                message=message, 
                info=utils.ErrorMessage.phone,
                )
        
        if str(message.chat.id) == GROUP_ID[1]:    
            if not utils.Check.max_lenght(message):
                bot.delete_message(message.chat.id, message.message_id)
                utils.send_info_message_and_delete_old_message(
                    message=message,
                    info=utils.ErrorMessage.lenght(message)
                )




if __name__ == '__main__':
    bot.infinity_polling()