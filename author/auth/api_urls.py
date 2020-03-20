from django.urls import path
from rest_auth import views as rest_auth_views
from author.auth import views as auth_views
from rest_auth.registration import views as rest_registration_views

urlpatterns = [
    path('login/', rest_auth_views.LoginView.as_view(), name='rest_login'),
    path('logout/', rest_auth_views.LogoutView.as_view(), name='rest_logout'),
    path('register/', rest_registration_views.RegisterView.as_view(), name='rest_register'),
    path('register/generate-code/', auth_views.CodeGenerationAPI.as_view(), name='email-verification-code'),
    path('password/reset/', rest_auth_views.PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/change/', rest_auth_views.PasswordChangeView.as_view(), name='rest_password_change'),

]
