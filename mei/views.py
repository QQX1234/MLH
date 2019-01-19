import hashlib
import random

import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mei.models import GoodList, GoodDetail, User, Cart


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
            # print(goodsid)
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
    except:

        return render(request, 'login.html')






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