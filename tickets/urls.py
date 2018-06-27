from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('insert', views.store_mail, name='insert'),
    path('sale', views.form_user, name='sale')
]
