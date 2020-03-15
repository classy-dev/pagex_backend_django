from rest_framework import routers
from django.urls import path
from blog import views

drf_router = routers.DefaultRouter()
drf_router.register('my-post', views.MyBlogPostViewSet, basename='my-blog-post')

urlpatterns = [
                  path('feed/', views.BlogPostFeedAPI.as_view(), name='blog-feed'),
              ] + drf_router.urls
