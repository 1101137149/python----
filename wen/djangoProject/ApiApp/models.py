from django.db import models

# Create your models here.
class Product(models.Model):
    #類別屬性
    id=models.IntegerField(primary_key=True) #整數 主鍵(不可重複)
    name=models.CharField(max_length=60) #字串最多60字
    price=models.IntegerField()

    def __str__(self):
        s=f'{self.id} {self.name} {self.price}'
        return  s