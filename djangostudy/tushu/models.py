from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_data = models.DateField()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)   #django版本后，外键一定要加on_delete


# Create your models here.
""""
图书表结构
表名：BookInfo
图书名称：btitle
图书发布时间：bpub_data

英雄表结构设计：
表名：HeroInfo
英雄姓名：hname
英雄性别：hgender
英雄简介：hcontent
所属图书：hbook    #外键

"""