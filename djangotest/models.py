from django.db import models
# 设计和表对应的模型类
# Create your models here.


# 图书类：一类
class BookInfo(models.Model):
    '''定义图书类'''
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    
    def __str__(self):
        # 返回书名
        return self.btitle


# 英雄人物类：多类
# 英雄名：hname，性别：hgender，年龄：hage，备注：hcomment
# 关系属性：建立图书类和人物类之间的一对多关系
class HeroInfo(models.Model):
    '''英雄人物模型类'''
    hname = models.CharField(max_length=20)
    # 性别：BooleanField说明是布尔类型，default指定默认值，False代表男
    hgender = models.BooleanField(default=False)
    # 英雄的备注
    hcomment = models.CharField(max_length=128)
    # 关系属性
    # 对应的表的字段名格式是：关系属性名_id
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    
    def __str__(self):
        # 返回英雄名
        return self.hname
