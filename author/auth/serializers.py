from django.conf import settings
from rest_framework import serializers
from rest_auth import serializers as auth_serializers
from rest_auth.registration import serializers as registration_serializers


class PasswordResetSerializer(auth_serializers.PasswordResetSerializer):
    def get_email_options(self):
        opts = {
            'from_email': settings.PASSWORD_RESET_FROM_EMAIL,

        }
        try:
            opts['email_template_name'] = settings.PASSWORD_RESET_CONFIRM_TEMPLATE_NAME
        except AttributeError:
            pass
        return opts


class RegisterSerializer(registration_serializers.RegisterSerializer):
    first_name = serializers.CharField(max_length=25)
    last_name = serializers.CharField(max_length=25)
    passion = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)

    def get_passion(self):
        from author.models import Passion
        try:
            passion, created = Passion.objects.get_or_create(name=self.validated_data['passion'])
            return passion
        except KeyError:
            return None

    def get_image(self):
        return self.validated_data.get('image')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        return data

    def save(self, request):
        from author.models import Profile
        user = super().save(request)
        Profile.objects.create(user=user, passion=self.get_passion(), image=self.get_image())
        return user
