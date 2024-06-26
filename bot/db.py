import orm_sqlite
from datetime import time

# DB classes
class BotDB(orm_sqlite.Model):
    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    chat_id = orm_sqlite.StringField(name='Chat ID', default='')
    user = orm_sqlite.StringField(name='User name', default='')


class CorrerctMessage(BotDB):
    message_id = orm_sqlite.IntegerField()
    message = orm_sqlite.StringField(name='Message', default='')
    date = orm_sqlite.StringField()
    phone = orm_sqlite.StringField(name='Phone', default='')


class BotMessage(BotDB):
    message_id = orm_sqlite.IntegerField(name='Message ID')


class CountUserMessage(BotDB):
    
    messge_id = orm_sqlite.IntegerField()
    
db = orm_sqlite.Database('bot.db')

BotDB.objects.backend = db

context = {
        # 'id': 1111,
        'chat_id': 123,
        'user': 'user_name',
        'message_id': 456,
        'message_id': 'my mesage',
        'date': time.now(),
        'phone': '+79083351669',
        }

if __name__ == '__main__':
    message = CorrerctMessage(context)
    message.save()
    CorrerctMessage.objects.all()