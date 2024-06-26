import utils
import config
import telebot


BOT_TOKEN = config.BOT_TOKEN
GROUP_ID = config.GROUP_ID
TARGET_CHANNEL = config.TARGET_CHANNEL
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(content_types = ['text'])
def spam_security(message):
    
    message_is_deleted = False
    if str(message.chat.id) in GROUP_ID\
        and str(message.from_user.username) not in config.SUPERUSERS:
    
    
        if not utils.Check.phone(message):
            bot.delete_message(message.chat.id, message.message_id)
            utils.send_info_message_and_delete_old_message(
                message=message, 
                info=utils.ErrorMessage.phone(),
                )
            utils.log(message=message)
            message_is_deleted = True
        
        if str(message.chat.id) == GROUP_ID[1]:    
            if not utils.Check.max_lenght(message):
                if not message_is_deleted:
                    bot.delete_message(message.chat.id, message.message_id)
                    utils.send_info_message_and_delete_old_message(
                        message=message,
                        info=utils.ErrorMessage.lenght(message)
                    )
                    message_is_deleted = True

            try:
                response = bot.get_chat_member(chat_id=TARGET_CHANNEL, user_id=int(message.from_user.id))
                if str(response.status) not in ['member', "creator"]:
                    if not message_is_deleted:
                        bot.delete_message(message.chat.id, message.message_id)
                        utils.send_info_message_and_delete_old_message(
                            message=message,
                            info=utils.ErrorMessage.subscribe_channel()
                        )
                        message_is_deleted = True

            except:
                print('user is not member')




if __name__ == '__main__':
    bot.infinity_polling()