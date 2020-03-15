from rest_framework import routers

from blog import views

drf_router = routers.DefaultRouter()
drf_router.register('my-post', views.MyBlogPostViewSet, basename='my-blog-post')

urlpatterns = [
              ] + drf_router.urls
