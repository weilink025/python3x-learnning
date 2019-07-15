from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=10)
    bpub_date = models.DateField(db_column=pub_date)
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table='book_wyb'
        ordering = ['id']  #正序  排序会增加数据库开销
        ordering = ['-id']  #降序

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

