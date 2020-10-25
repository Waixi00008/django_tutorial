from django.db import models
from django_redis import get_redis_connection

from functools import wraps
import json
import time

_cache = get_redis_connection('default')

# 缓存值
def cache(func):
    @wraps(func)
    def wrapper(obj,*args):
        key = args[0]
        value = _cache.get(key)
        if value:
            return json.loads(value)
        rs = func(obj,*args)
        _cache.set(key,json. dumps(rs))
        return rs
    return wrapper

class User(models.Model):
    username = models.CharField(unique=True, max_length=20, default='')
    age = models.SmallIntegerField(default=0)
    phone = models.IntegerField(db_index=True, blank=True, default=0)
    email = models.EmailField(blank=True, default='')
    info = models.TextField(default='')
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta: #创建联合索引
        index_together = ['username','phone']

    def __str__(self):
        return 'user:{}'.format(self.username)

    @classmethod
    @cache
    def get(cls,id):
        rs=cls.objects.get(id=id)
        return {
            'id':rs.id,
            'username':rs.username,
            'age':rs.age,
            'email':rs.email,
            'info':rs.info,
            'created_time':str(rs.created_time),
            'updated_time':str(rs.updated_time)
        }

# 与user一对一关系，表创建出id,birthday,usre_id字段
class Userprofile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    birthday = models.CharField(max_length=100, default='')
# 与user一对多关系，表创建出id,content,create_time,usre_id字段
class Diary(models.Model):
    user = models.ForeignKey(User,related_name='diary',null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_time = models.IntegerField()

# 与user多对多关系，生成两张表 app_group和app_group_user
# app_group有id,name,created_time
# app_group_user有id,group_id,user_id
class Group(models.Model):
    user = models.ManyToManyField(User,related_name='group')
    name = models.CharField(max_length=20)
    created_time = models.IntegerField()

class Message(models.Model):
    content = models.TextField()
    message_type = models.CharField(max_length=10,db_index=True)
    created_time = models.IntegerField(default=0)

    def __str__(self):
        return 'type:{},content:{}'.format(self.message_type,self.content)

    def times(self):
        _time = time.localtime(self.created_time)
        return time.strftime('%Y-%m-%d %H:%M:%S',_time)
