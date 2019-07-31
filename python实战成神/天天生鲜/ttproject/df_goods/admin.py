from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.
#管理商品分类和商品


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    def upload_ppic(self, obj):
        try:
            img = mark_safe('<a href="%s" target="_blank"><img src="%s" width="100px" height="100px"  /></a>' % (obj.ppic.url,obj.ppic.url))
        except Exception as e:
            img = ''
        return img
    list_display = ['id','pname','ptype','pbrief','upload_ppic','pprice','pstock','punit','pclick','precommend']
    list_per_page = 20
    search_fields = ['pname']
    upload_ppic.short_description = '图片'
    upload_ppic.allow_tags = True

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):

    def upload_icon(self, obj):
        try:
            img = mark_safe('<a href="%s" target="_blank"><img src="%s" width="100px" height="100px"  /> </a>' % (obj.ticon.url,obj.ticon.url))
        except Exception as e:
            img = ''
        return img

    def upload_pic(self, obj):
        try:
            img = mark_safe('<a href="%s" target="_blank"><img src="%s" width="100px" height="100px"  /> </a>' % (obj.tpic.url,obj.tpic.url))
        except Exception as e:
            img = ''
        return img
    upload_icon.short_description = '图标'
    upload_icon.allow_tags = True

    upload_pic.short_description = '推荐图'
    upload_pic.allow_tags = True


    list_display = ['id', 'ttitle', 'upload_icon','upload_pic']
    list_per_page = 20
    readonly_fields = ['upload_icon']
    readonly_fields = ['upload_pic']






