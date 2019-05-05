from django.contrib import admin
from djangotest.models import BookInfo, HeroInfo


# 后台管理页面
# Register your models here.
# 自定义模型管理类
class BookInfoAdamin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id', 'btitle', 'bpub_date']
    
    
class HeroInfoAdamin(admin.ModelAdmin):
    '''英雄人物模型管理类'''
    list_display = ['id', 'hname', 'hcomment']
    
    
# 注册模型类
admin.site.register(BookInfo, BookInfoAdamin)
admin.site.register(HeroInfo, HeroInfoAdamin)
