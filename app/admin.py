import time

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Message
# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','content','message_type','created_time','times','operate','image_data']
    list_filter = ('message_type',)
    search_fields = ['content']
    ordering = ['-id']
    list_per_page = 5

    # 二次处理数据
    def save_model(self,request,obj,form,change):
        if change:
            obj.content = obj.content+'update'
        else:
            obj.content = obj.content+'create'
            # print(datetime.date(2020,10,25))
            obj.created_time = time.time()
        super(MessageAdmin,self).save_model(request,obj,form,change)

    # 处理字段格式
    def operate(self,obj):
        return format_html('<a href="{}"/>跳转','https://www.baidu.com')
    
    # 处理字段表现形式 同operate
    def image_data(self,obj):
        return mark_safe(u'<img src="%s" width="50px" height=“50px” />'%'https://i3.hoopchina.com.cn/hupuapp/bbs/153/31492153/thread_31492153_20201025091314_s_37103_o_w_520_h_640_1880.jpg?x-oss-process=image/resize,w_800')