from django.conf.urls import url

from mei import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^detail/(\(d+)/$',views.detail,name='detail'),
    url(r'^goods/$',views.goods,name='goods'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),


    # url(r"^goodgoods/$",views.goodgoods,name='goodgoods'),
]