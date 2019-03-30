from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url('Objective_id/(\d+)/', views.objective_detail, name='key_result_detail'),
]
