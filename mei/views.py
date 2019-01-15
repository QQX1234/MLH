import hashlib
import random

import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from mei.models import GoodList, GoodDetail, User


def index(request):
    return render(request,'index.html')


def cart(request):
    return render(request,'cart.html')


def detail(request,gooddetailid):

   gooddetail = GoodDetail.objects.get(id=gooddetailid)


   return render(request,'detail.html',{'gooddetail':gooddetail})


def goods(request):

    goodlists = GoodList.objects.all()



    return render(request,'goods.html',{'goodlists':goodlists})


def generate_token():
    md5 = hashlib.md5()
    tempstr = str(time.time()) + str(random.random())
    md5.update(tempstr.encode('utf-8'))
    return md5.hexdigest()


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

        request.session['token'] = generate_token()

        return redirect('mei:index')


def generate_password(password):

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()



def login(request):

    if request.method == 'GET':
        return render(request,'login.html')

    elif request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == generate_password(password):
                token = generate_token()
                user.save()
                request.session['token'] = generate_token()

                return redirect('mei:index')
            else:
                return render(request,'login.html',context={'err':'密码错误'})

        except:
            return render(request,'login.html',context={'err':'账户有误'})






    return render(request,'login.html')


def logout(request):

    request.session.flush()

    return redirect('index.html')



def checkemail(request):
    email = request.GET.get('email')

    users = User.objects.filter(email=email)

    if users.exists():
        return JsonResponse({'msg':'账号被占用','status':0})
    else:
        return  JsonResponse({'msg':'账号可以用','status':1})
