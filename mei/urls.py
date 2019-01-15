from django.conf.urls import url

from mei import views

urlpatterns=[
    url(r'^$',views.index,name='index'),   #首页
    url(r'^cart/$',views.cart,name='cart'),  #购物车
    url(r'^detail/(\d+)$',views.detail,name='detail'),  #详情页
    url(r'^goods/$',views.goods,name='goods'),   #商品列表
    url(r'^register/$',views.register,name='register'),   #注册页面
    url(r'^login/$',views.login,name='login'),      #登录页面
    url(r'^logout/$',views.logout,name='logout'),   #退出页面
    url(r'^checkemail/$',views.checkemail,name='checkemail'),  #核对手机号

]