from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_list, name='cart_list'),
]