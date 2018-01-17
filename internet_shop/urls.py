from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_list, name='cart_list'),
    url(r'^product/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^product/new/$', views.product_new, name='product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$', views.product_edit, name='product_edit'),
]

