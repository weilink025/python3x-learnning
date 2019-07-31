from django.db import models

# Create your models here.
class CartInfo(models.Model):
    order_pro_id = models.ForeignKey('df_goods.ProductInfo',on_delete= 'CASCADE')
    order_user_id = models.ForeignKey('df_user.UserInfo',on_delete= 'CASCADE')
    count = models.IntegerField()

