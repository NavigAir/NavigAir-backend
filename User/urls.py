from django.urls import path
from User.views import views

urlpatterns = [
    path('', views.userList, name='list_users'),
    path('unit', views.users, name='users'),
]