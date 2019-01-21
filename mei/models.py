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

    class Meta:
        db_table = 'mei_cart'



class Order(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 状态
    # -2 退款
    # -1 过期
    # 0 未付款
    # 1 已付款，未发货
    # 2 已付款，已发货
    # 3 已签收，未评价
    # 4 已评价
    status = models.IntegerField(default=0)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    # 订单号
    identifier = models.CharField(max_length=256)

    class Meta:
        db_table = 'mei_order'



# 订单商品 模型类
# 一个订单 对应 多个商品
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(GoodDetail)
    # 商品规格
    number = models.IntegerField()

    class Meta:
        db_table = 'mei_ordergoods'