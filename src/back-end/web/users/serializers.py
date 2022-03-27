from .models import users, social_types
from rest_framework import serializers


class SocialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = social_types
        fields = '__all__'
        extra_kwargs = {
            'name': {
                'read_only': True
            },
            'logoKey': {
                'read_only': True
            }
        }


class UserSerializer(serializers.ModelSerializer):
    social_type = SocialTypeSerializer()
    # account = AccountSerializer()

    class Meta:
        model = users
        fields = '__all__'
        read_only_fields = [
            'nickname'
            'email',
            'cellPhoneNumber',
            'birthday',
            'isBlocked',
            'registrationDateTime',
            'withdrawalDateTime'
        ]
