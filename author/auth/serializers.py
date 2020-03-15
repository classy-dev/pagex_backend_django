from django.conf import settings
from rest_auth import serializers as rest_auth_serializers


class PasswordResetSerializer(rest_auth_serializers.PasswordResetSerializer):
    def get_email_options(self):
        opts = {
            'from_email': settings.PASSWORD_RESET_FROM_EMAIL,

        }
        try:
            opts['email_template_name'] = settings.PASSWORD_RESET_CONFIRM_TEMPLATE_NAME
        except AttributeError:
            pass
        return opts
