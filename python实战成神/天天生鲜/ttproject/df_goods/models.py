from django.db import models
from DjangoUeditor.models import UEditorField

# 产品类型
class ProductType(models.Model):
    ttitle = models.CharField(max_length=20,verbose_name='类别')    #类名
    tpic = models.ImageField(upload_to='df_goods',default=False,verbose_name='推荐图片')    #首页分类图片
    ticon = models.ImageField(upload_to='df_goods',default=False,verbose_name='类别图标')    #分类图标
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'producttype'
        verbose_name = '商品分类信息'
        verbose_name_plural = '商品分类信息'

    def __str__(self):
        return self.ttitle


#产品信息

class ProductInfo(models.Model):
    pname = models.CharField(max_length=20,verbose_name='品名')
    ptype = models.ForeignKey('ProductType',on_delete='CASCADE',verbose_name='所属类')
    pbrief = models.CharField(max_length=200,verbose_name='简介')
    ppic = models.ImageField(upload_to='df_goods',verbose_name='图片')
    pprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')
    pstock = models.IntegerField(verbose_name='库存',default=0)    #库存
    punit = models.CharField(max_length=20,verbose_name='单位')
    pclick = models.IntegerField(verbose_name='点击量')    #点击量
    precommend = models.BooleanField(default=False,verbose_name='是否推荐')  #是否推荐
    pnew_recommend = models.BooleanField(default=False, verbose_name='新品推荐')  # 新品推荐
    pcontent = UEditorField('商品详情',height=600,width=1024,imagePath="uploadimg/",toolbars='full',filePath='upload/',blank=True)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'productinfo'
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
    def __str__(self):
        return self.pname


