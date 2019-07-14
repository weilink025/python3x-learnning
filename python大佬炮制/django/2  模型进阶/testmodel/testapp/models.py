from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=10)
    bpub_date = models.DateField()

class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

