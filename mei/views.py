import hashlib
import random

import time
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mei.alipay import alipay
from mei.models import GoodList, GoodDetail, User, Cart, Order, OrderGoods


# 魅力惠首页
def index(request):

    try:
        token = request.session.get('token')

        if token:
            user = User.objects.get(token=token)

        return render(request, 'index.html', context={'user': user})
    except:

        return render(request, 'index.html',context={'user':None})


# 购物车
def cart(request,goodsid):

    # 获取token

    try:
        token = request.session.get('token')

        if token:
            user = User.objects.get(token=token)

            # goodsid = request.GET.get('goodsid')
            print(goodsid)
            goods = GoodDetail.objects.get(pk=goodsid)
            # print(goods.src1)
            carts = Cart.objects.filter(user=user).exclude(number=0)
            print(carts.count())

            data = {
                'user': user,
                'carts': carts,
                'goods': goods
            }

            return render(request, 'cart.html', context=data)
            # return redirect('mei:cart',data)
        else:
            return render(request, 'login.html')
    except:

        return render(request, 'login.html')
        # return redirect('mei:login')





# 商品详情
def detail(request,gooddetailid):

   gooddetail = GoodDetail.objects.get(id=gooddetailid)
   carts = []

   try:
       token = request.session.get('token')

       if token:
           user = User.objects.get(token=token)
           carts = Cart.objects.filter(user=user)

           data = {
               'gooddetail': gooddetail,
               'user':user,
               'carts': carts
           }

       return render(request, 'detail.html', data)

   except:
       data = {
           'gooddetail': gooddetail,
           'user': None,

       }

       return render(request, 'detail.html', data)








# 商品列表
def goods(request):

    goodlists = GoodList.objects.all()

    try:
        token = request.session.get('token')

        if token:
            user = User.objects.get(token=token)

            data = {
                'goodlists': goodlists,
                'user': user
            }

        return render(request, 'goods.html', data)

    except:
        data = {
            'goodlists': goodlists,
            'user': None
        }

        return render(request, 'goods.html', data)






#令牌加密
def generate_token():
    md5 = hashlib.md5()
    tempstr = str(time.time()) + str(random.random())
    md5.update(tempstr.encode('utf-8'))
    return md5.hexdigest()




# 注册
def register(request):

    if request.method == 'GET':

        return render(request,'register.html')

    elif request.method == 'POST':

        user = User()

        user.email = request.POST.get('email')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.phone = request.POST.get('phone')

        user.token = generate_token()

        user.save()

        request.session['token'] = user.token

        return redirect('mei:index')



#密码加密
def generate_password(password):

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()




# 登录
def login(request):

    if request.method == 'GET':
        return render(request,'login.html')

    elif request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == generate_password(password):
                user.token = generate_token()
                user.save()
                request.session['token'] = user.token

                return redirect('mei:index')
            else:
                return render(request,'login.html',context={'err':'密码错误'})

        except:
            return render(request,'login.html',context={'err':'账户有误'})


    return render(request,'login.html')




# 退出登录
def logout(request):

    request.session.flush()

    return redirect('mei:index')




# 查看邮箱是否注册过
def checkemail(request):
    email = request.GET.get('email')

    users = User.objects.filter(email=email)

    if users.exists():
        return JsonResponse({'msg':'账号被占用','status':0})
    else:
        return  JsonResponse({'msg':'账号可以用','status':1})


def addcart(request):

    token = request.session.get('token')

    if token:

        user = User.objects.get(token=token)

        goodsid = request.GET.get('goodsid')
        #
        # print("1"+ goodsid )
        goods = GoodDetail.objects.get(pk=goodsid)

        carts = Cart.objects.filter(user=user).filter(goods=goods)


        if carts.exists():   #存在则修改ｎｕｍｂｅｒ
            cart = carts.first()

            cart.number = cart.number + 1
            cart.save()
            responseData = {
                'status': 1,
                'number': cart.number,
            }

        else:  #添加一条新纪录
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1

            cart.save()
            responseData = {
                'msg': '{}-添加购物车成功!'.format(goods.title),
                'status': 1,
                'number': cart.number,
                'gooddetail':goods
            }

        return JsonResponse(responseData)


    else:
        return JsonResponse({'msg': '请登录后操作!', 'status': 0})






def subcart(request):

    token = request.session.get('token')

    user = User.objects.get(token=token)
    # print(user)
    goodsid = request.GET.get('goodsid')

    goods = GoodDetail.objects.get(pk=goodsid)

    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.number = cart.number -1
    # print(cart.number)
    cart.save()

    responseData = {
        'msg': '{}-商品删减成功'.format(goods.title),
        'status': 1,
        'number': cart.number,
        # 'gooddetail': goods
    }
    # print(responseData)
    return JsonResponse(responseData)


def changecartstatus(request):

    cartid = request.GET.get('cartid')

    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    data = {
        'msg': '状态修改成功',
        'status': 1,
        'isselect': cart.isselect
    }

    return JsonResponse(data)



def changecartall(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)

    # True/False
    isall = request.GET.get('isall')
    if isall == 'true':
        isall = True
    else:
        isall = False

    carts = Cart.objects.filter(user=user).update(isselect=isall)

    data = {
        'msg': '状态修改成功',
        'status': 1,
    }

    return JsonResponse(data)


def generate_identifire():
    tempstr = str(int(time.time())) + str(random.random())
    return tempstr


def generateorder(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)

    # 订单
    order = Order()
    order.user = user
    order.identifier = generate_identifire()
    order.save()

    # 订单商品
    carts = Cart.objects.filter(user=user).filter(isselect=True).exclude(number=0)
    # 只有选中的商品，才是添加到订单中，从购物车中删除
    for cart in carts:
        orderGoods = OrderGoods()
        orderGoods.order = order
        orderGoods.goods = cart.goods
        orderGoods.number = cart.number
        orderGoods.save()

        # 从购物车中删除
        cart.delete()

    data = {
        'msg': '下单成功',
        'status': 1,
        'identifier': order.identifier
    }

    return JsonResponse(data)


def orderdetail(request, identifier):
    order = Order.objects.get(identifier=identifier)

    return render(request, 'orderdetail.html', context={'order': order})

@csrf_exempt
def appnotify(request):
    # http://112.74.55.3/axf/returnview/?charset=utf-8&out_trade_no=15477988300.6260414050156342&method=alipay.trade.page.pay.return&total_amount=93.00&sign=oaTJZPDeswBfEbQGkBND8w8DDOWGMdz8lw6TlL25Sp73TZtTBqUBx2vazVi5sI6pFLSgfF%2FRsxsiY20S5UzZeCJ5hfrGXp4NCg6ZpZE%2FWS1CsMnI74lO%2F8ttTx1j%2FzfhrJJuTIHJ503Z1wiDZoXHer91ynI%2FCTLn8W0de2fVhnBi5hTo7MJHJBZQnVQ%2BnFJ73cKBB16xdIJ15ISVUrYYi%2FUGJr2jh%2BllGiiTVm4o0maDuYH3ljuGVxAI4yvP%2BevAfo7B2MK%2F1BW3%2FVu8JRLatEIqeyV2Qk87%2F%2FGRndFRjRDuuZMU8zzix0eg0oKYVeBmfOnRPXhMFAs8dGPedC1D2Q%3D%3D&trade_no=2019011822001416700501217055&auth_app_id=2016091800542542&version=1.0&app_id=2016091800542542&sign_type=RSA2&seller_id=2088102176233911&timestamp=2019-01-18+16%3A08%3A08

    # 获取订单号，并且修改订单状态
    if request.method == 'POST':
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)
        post_dir = {}

        print(body_str)
        print(post_data)
        print(post_data.items())
        for key, value in post_data.items():
            post_dir[key] = value[0]

        out_trade_no = post_dir['out_trade_no']
        print(out_trade_no)

        # 更新状态
        Order.objects.filter(identifier=out_trade_no).update(status=1)

        return JsonResponse({'msg': 'success'})


def returnview(request):

    return redirect('mei:index')


def pay(request):
    identifier = request.GET.get('identifier')
    order = Order.objects.get(identifier=identifier)

    sum = 0
    for orderGoods in order.ordergoods_set.all():

        sum += int(orderGoods.goods.pri)* orderGoods.number

    # 支付地址
    url = alipay.direct_pay(
        subject='魅力惠－包包',  # 支付宝页面显示的标题
        out_trade_no=identifier,  # AXF订单编号
        total_amount=str(sum),  # 订单金额
        return_url='http://47.107.167.189/mei/returnview/'
    )

    # 拼接上支付网关
    alipayurl = 'https://openapi.alipaydev.com/gateway.do?{data}'.format(data=url)

    return JsonResponse({'alipayurl': alipayurl, 'status': 1})


def orderlist(request, status):
    orders = Order.objects.filter(status=status)

    return render(request, 'orderlist.html', context={'orders': orders})

