from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_result/', views.add_result, name='add_result'),
    path('edit_result/<int:pk>/', views.edit_result, name='edit_result'),
    path('delete_result/<int:pk>/', views.delete_result, name='delete_result'),
    path('verify_email/<uuid:token>/', views.verify_email, name='verify_email'),
    path('onboarding/', views.onboarding, name='onboarding'),
]
