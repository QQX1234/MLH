from django.http import HttpResponse
from django.shortcuts import render


from mei.models import GoodList, GoodDetail


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


def register(request):



    return render(request,'register.html')


def login(request):



    return render(request,'login.html')


def logout(request):
    return render(request,'index.html')


# def goodgoods(request):
#
#     return render(request, 'goodgoods.html')