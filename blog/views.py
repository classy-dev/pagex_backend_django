from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostListSerializer


class MyBlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

    def get_serializer_class(self):
        return BlogPostListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostFeedAPI(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListSerializer
