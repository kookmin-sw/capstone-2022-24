from rest_framework import serializers
from .models import video_providers

class videosSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    video_id = serializers.IntegerField()
    provider_id = serializers.IntegerField()
    link = serializers.URLField()
    offer_date= serializers.DateField()
    deadline= serializers.DateField()

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return video_providers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.offerType = validated_data.get('offerType', instance.offerType)
        instance.link = validated_data.get('link', instance.link)
        instance.offerDate = validated_data.get('offerDate', instance.offerDate)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.save()
        return instance

    class Meta:
        model = video_providers
        fields = ['videoId', 'offerType', 'link', 'offerDate', 'deadline']
