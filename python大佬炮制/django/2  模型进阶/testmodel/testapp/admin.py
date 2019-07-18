from django.contrib import admin
from .models import *
# Register your models here.
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3
class BookInfoAdmin(admin.ModelAdmin):
    inlines = [HeroInfoInline]
    list_display = ['id','bpub_date','btitle']
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcontent','hbook']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)