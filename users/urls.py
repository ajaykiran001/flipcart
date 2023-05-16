from django.urls import path
from . import views

app_name = 'users'
urlpatterns=[
    path('buy',views.buy,name='buy'),
]