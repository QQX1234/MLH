from django.db import models



# 商品列表
class GoodList(models.Model):
    productid = models.CharField(max_length=40)
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



# 商品详情表
class GoodDetail(models.Model):
    productid = models.CharField(max_length=40)
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


# 用户信息
class User(models.Model):
    # 邮箱 【邮箱登录】
    email = models.CharField(max_length=20, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 名字
    name = models.CharField(max_length=100)
    # 手机号
    phone = models.CharField(max_length=20)

    # 令牌
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'mei_user'


 # 购物车
class Cart(models.Model):

    user = models.ForeignKey(User)

    goods = models.ForeignKey(GoodDetail)

    number = models.IntegerField()

    isselect = models.BooleanField(default=True)