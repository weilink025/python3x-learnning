from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete = True)

    def create(self,title,pub_date):
        book = self.model()
        book.btitle = title
        book.bpub_date=pub_date
        book.bread = 0
        book.bcommet =0
        book.isDelete = False
        return book






class BookInfo(models.Model):
    btitle = models.CharField(max_length=10)
    bpub_date = models.DateField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    books = BookInfoManager()
    class Meta:
        db_table='book_wyb'
      #  ordering = ['id']  #正序  排序会增加数据库开销
       # ordering = ['-id']  #降序
    """
    @classmethod
    def create(cls,title,pub_date):
        book = cls(btitle=title,bpub_date=pub_date)
        book.bread=0
        book.bcommet=0
        book.isDelete=False
        return book
"""
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


