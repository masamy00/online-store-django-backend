# your_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('staticdata/', views.no_rest_no_model, name='example'),
    path('allproducts/', views.FBV_list, name='allproducts')

]
