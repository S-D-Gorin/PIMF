import telebot
import config
import re


bot = telebot.TeleBot(config.BOT_TOKEN)


#  Defined write in .TXT database
def db_write(db_name, mode, data):
    with open(f'{config.DB_PATH + db_name}', mode=mode, encoding='utf-8') as db:
        db.write(data)



#  Get username from message
def get_user_name(message):
    if message.from_user.username == None:
        user = message.from_user.first_name
    else:
        user = f'@{message.from_user.username}'
        
    return user



#  Склонение слова 'символ' написал @Olegdev8
def last_char(num):
    a = int(num)
    if 2 <= a % 10 <= 4 and not 12 <= a % 100  <= 14:
        b = 'символа'
    elif a % 10 == 1 and a % 100 != 11:
        b = 'символ'
    else:
        b = 'символов'
    return b




#  Send answer message in chat 
def send_info_message_and_delete_old_message(message, info):
    
    # имя пользователя отправившего сообщение не прошедшее проверку
    user = get_user_name(message)


    # отправка сообщения о том, что сообщение удалено и 
    # получение айди отправленного сообщения
    id_to_delete = bot.send_message(
        message.chat.id, 
        f'{user} - ваше сообщение удалено. \n ▪️Чтобы отправить сообщение, {info}', 
        protect_content=True, 
        disable_notification=True
        ).message_id
    
    
    # запись айди отправленнного ботом сообщения в базу данных
    db_write(f'id_bm_from_{message.chat.id}.txt', 'a', f'{id_to_delete}\n')
    
    # извлечение айди предпоследнего сообщения от бота
    with open(
        f'{config.DB_PATH}id_bm_from_{message.chat.id}.txt', 'r', encoding='utf-8') as bot_message_id:
        
        message_id = bot_message_id.readlines()[-2]
        
        # удаление сообщения с выбранным айди
        bot.delete_message(message.chat.id, int(message_id))

def log(message):
    username = get_user_name(message=message)
    spam = message.text
    user_id = message.from_user.id
    db_write(
        db_name=f'spam_from_chat{message.chat.id}.txt',
        mode="a",
        data=f"User: {username} \n User_id: {user_id} \n Spam: {spam} \n"
        )
    

class ErrorMessage:
    
    def phone():
        error_information = 'добавьте номер телефона в объявление (Начиная с +7 или 8)'
        return error_information

    
    def lenght(message):
        extra_chars = len(str(message.text)) - config.MAX_LENGHT
        error_information = f'\
                    сократите его на {extra_chars} {last_char(extra_chars)}. \
                    По вопросам рекламы в чате обращаться @Nikita_SOMIO22'
        return error_information
    
    def subscribe_channel():
        error_information = 'Подпишитесь на канал @tenderlar23 чтобы отправить сообщение'
        return error_information



class Check:
    def phone(message):
        if re.search(r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})', message.text):
            return True
        
        
    def max_lenght(message):
        if len(str(message.text)) <= config.MAX_LENGHT:
            return True