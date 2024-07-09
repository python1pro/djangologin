from django.urls import path
from . import views

urlpatterns = [         
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('panel/', views.AdminPanel, name= 'panel'), 
    path('adminlogin/', views.AdminLogin, name='adminlogin'),
    path('add/', views.Add, name = 'add' ),
    path('edit/', views.Edit, name = 'edit'), 
    path('update/<str:id>/', views.Update, name='update'), 
    path('delete/<str:id>/', views.Delete, name='delete' ),
    path('adminlogout/', views.AdminLogout, name='adminlogout')
]