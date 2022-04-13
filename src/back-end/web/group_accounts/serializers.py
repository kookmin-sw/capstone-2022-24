from rest_framework import serializers
from .models import GroupAccount


class GroupAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAccount
        fields = '__all__'
        read_only_fields = [
            'creationDateTime',
            'lastModificationDateTime'
        ]
