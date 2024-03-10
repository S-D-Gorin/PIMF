#  После работы в тестовом режиме проверить суперюзеров
#  обслуживаемые группы и бот токен
#  

DB_PATH = './databases/'


DEBUG = True

if DEBUG:
    # My test bot
    BOT_TOKEN = '6499225383:AAGHpQKw6FVcKVvJYL_TM-dMwpoqRDCNzK4'
else:
    # ChatPolice bot
    BOT_TOKEN = '6629159570:AAHo1KKdW-AaofcUpw-1GjHBeK1j3EYWpsM'

# My chats
GROUP_ID = (
    'None',
    '-1001901700124',  # Test Chat
    # '-1001647209747',  # SOMIO
    # '-1001928504949',  # Monolit
    ) 

SUPERUSERS = (
    # 'sdg9999',
    'Nikita_SOMIO22',
)


MAX_LENGHT = 222






future_group_settings = {'SOMIO':{
    
    'superusers': [        
        'Nikita_SOMIO22',
        'sdg9999',
        ]
    },

    'checks': [
        'phone_number',
        'lenght',
        ]
}