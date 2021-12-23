from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('home/', views.home, name='home'),
    path('logout/', views.auth_logout, name='logout'),
    path('add/', views.add_resource, name='add_resource'),
    path('doubt/', views.doubt, name='doubt'),
    path('doubt-add/', views.doubt_add, name='doubt_add'),
    path('doubt-view/<int:pk>/', views.doubt_view, name='doubt_view'),
    path('notification/', views.notification, name='notification'),
    path('notification-add/', views.notification_add, name='notification_add'),
    path('resource/', views.resource, name='resource'),
    path('admin_resource/', views.admin_resource, name='admin_resource'),
    path('qr/', views.qr, name='qr'),
    path('contact/', views.contact, name='contact'),
]