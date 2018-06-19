from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.nth_number, name='fibonaccii_nth_number'),
]
