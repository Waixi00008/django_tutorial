from django.db import models


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