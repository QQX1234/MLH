import hashlib
import random

import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mei.models import GoodList, GoodDetail, User


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
def cart(request):

    # 获取token

    token = request.session.get('token')
    user = None
    if token:
        user = User.objects.get(token=token)

        return render(request, 'cart.html', context={'user': user})
    else:
        return render(request,'login.html')





# 商品详情
def detail(request,gooddetailid):

   gooddetail = GoodDetail.objects.get(id=gooddetailid)

   try:
       token = request.session.get('token')

       if token:
           user = User.objects.get(token=token)

           data = {
               'gooddetail': gooddetail,
               'user':user
           }

       return render(request, 'detail.html', data)

   except:
       data = {
           'gooddetail': gooddetail,
           'user': None
       }

       return render(request, 'detail.html', data)



   # return render(request,'detail.html',{'gooddetail':gooddetail})




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


    # return render(request,'goods.html',{'goodlists':goodlists})




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
