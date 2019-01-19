from django.conf.urls import url

from mei import views

urlpatterns=[
    url(r'^$',views.index,name='index'),   #首页
    url(r'^cart/(\d+)/$',views.cart,name='cart'),  #购物车
    url(r'^detail/(\d+)/$',views.detail,name='detail'),  #详情页
    url(r'^goods/$',views.goods,name='goods'),   #商品列表


    url(r'^register/$',views.register,name='register'),   #注册页面
    url(r'^login/$',views.login,name='login'),      #登录页面
    url(r'^logout/$',views.logout,name='logout'),   #退出页面
    url(r'^checkemail/$',views.checkemail,name='checkemail'),  #核对邮箱

    url(r'^addcart/$',views.addcart,name='addcart'),    #购物车加操作
    url(r'^subcart/$', views.subcart, name='subcart'),  #购物车减操作

    # 更改购物车商品状态
    url(r'^changecartstatus/$',views.changecartstatus,name='changecartstatus'),
    # 是否全选
    url(r'^changecartall',views.changecartall,name='changecartall'),
]