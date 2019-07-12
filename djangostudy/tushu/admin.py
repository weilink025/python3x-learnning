from django.contrib import admin
from .models import *

# Register your models here.
#关联对象
#class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline):   #表格效果
    model = HeroInfo
    extra = 2



class BookInfoAdmin(admin.ModelAdmin):

    inlines = [HeroInfoInline]   #关联对象

    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']      #右侧过滤器
    list_per_page = 5             #分页每页显示数量
    search_fields = ['btitle']    #可以以什么字段搜索

    #详细修改内页定制
    #fields = ['bpub_date','btitle']
    fieldset = ([
        ('base',{'fields':['btitle']})],
        [ ('super', {'fields': ['bpub_date']})])



class HeroInfoAdmin(admin.ModelAdmin):



    list_display = ['id','hname','hgender','hcontent','hbook']

    list_filter = ['hname']  # 右侧过滤器
    list_per_page = 5  # 分页每页显示数量
    search_fields = ['hname']  # 可以以什么字段搜索

    # 详细修改内页定制
    #fields = ['hname','hgender','hcontent','hbook']
    fieldset = [
        ('base', {'fields': ['hname','hgender']}),
        ('super', {'fields': ['hcontent','hbook']})
    ]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)