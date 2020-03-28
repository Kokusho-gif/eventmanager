from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.listfunc, name='list'),
    path('signup/', views.signupfunc, name='signup'),
    path('logout/', views.logoutfunc, name='logout'),
    path('login/', views.loginfunc, name='login'),
    path('login/<int:event_pk>/', views.loginfunc, name='login'),
    path('mypage/<int:current_status>/', views.usermypagefunc, name='mypage'),
    path('createevent/',views.createeventfunc, name='createevent'),
    path('detail/<int:event_pk>/', views.detailfunc, name='detail')
    # path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
]
