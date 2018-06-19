from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.NthNumber.as_view(), name='fibonaccii_nth_number'),
]
