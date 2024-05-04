from django.urls import path
from User.views import views, check_in

urlpatterns = [
    path('', views.userList, name='list_users'),
    path('unit', views.users, name='users'),
    path('checkin', check_in.checkIns, name='check_in'),
]