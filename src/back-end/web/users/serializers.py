from .models import User, SocialType
from rest_framework import serializers


class SocialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialType
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
        model = User
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
