from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Passion

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile.image', required=False)
    passion = serializers.CharField(source='profile.passion.name', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'passion', 'image')
        read_only_fields = ('email',)

    def _get_passion(self, name):
        try:
            return Passion.objects.get(name=name)
        except Passion.DoesNotExist:
            return None

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile', {})
        instance.profile.image = profile.get('image', instance.profile.image)
        instance.profile.passion = self._get_passion(profile.get('passion', {}).get('name'))
        instance.profile.save()
        return super().update(instance, validated_data)
