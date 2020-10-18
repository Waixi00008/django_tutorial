from mongoengine import Document,StringField,IntField
from django.conf import settings

class User(Document):
    db = settings.MONGOCLIENT['user']
    name = StringField(required=True,max_length=200)
    age = IntField(required=True)
    # 指明连接的数据表名
    meta = {'collection': 'user'}