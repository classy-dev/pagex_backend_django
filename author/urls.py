from django.urls import path
from author import views

urlpatterns = [
    path('who-am-i/', views.UserAPI.as_view(), name='user-detail')
]
