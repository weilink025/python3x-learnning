from django.db import models

# Create your models here.
"""
Date:2019-7-23
Author:wade

"""
#商城用户模型
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)    #sha加密方式 md5 是16位
    uemail = models.CharField(max_length=30)
    ureceiver = models.CharField(max_length=20,default='')
    uaddress = models.CharField(max_length=100,default='')
    upostcode = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')
    class Meta:
        db_table = 'user_info'

