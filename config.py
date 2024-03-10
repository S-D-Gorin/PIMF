import os

#  После работы в тестовом режиме проверить суперюзеров
#  обслуживаемые группы и бот токен
#  

DB_PATH = './databases/'


# DEBUG = False
DEBUG = True

if DEBUG:
    # My test bot
    BOT_TOKEN = os.getenv('TEST_BOT_TOKEN')
else:
    # ChatPolice bot
    BOT_TOKEN = os.getenv('BOT_TOKEN')


# My chats
GROUP_ID = (
    # 'None',
    '-1001901700124',  # Test Chat
    '-1001647209747',  # SOMIO
    '-1001928504949',  # Monolit
    ) 

SUPERUSERS = (
    'sdg9999',
    'Nikita_SOMIO22',
    'hardcorno', 
    'OlegBKzn',
    'MONOLITKAZANN',
)


MAX_LENGHT = 222