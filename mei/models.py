from django.db import models

class GoodList(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    buyer = models.CharField(max_length=40)
    src1 = models.CharField(max_length=80)
    src2 = models.CharField(max_length=80)
    src3 = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    original_price = models.CharField(max_length=40)
    index1 = models.CharField(max_length=80)
    index2= models.CharField(max_length=80)
    index3 = models.CharField(max_length=80)

    def __str__(self):
        return self.title




class GoodDetail(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    buyer = models.CharField(max_length=40)
    src1 = models.CharField(max_length=80)
    src2 = models.CharField(max_length=80)
    src3 = models.CharField(max_length=80)
    src4 = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=40)
    pri = models.CharField(max_length=40)
    original_price = models.CharField(max_length=40)
    index1 = models.CharField(max_length=80)
    index2= models.CharField(max_length=80)
    index3 = models.CharField(max_length=80)
    index4 = models.CharField(max_length=80)

    def __str__(self):
        return self.title