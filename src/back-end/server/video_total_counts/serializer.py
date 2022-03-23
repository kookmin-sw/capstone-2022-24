from rest_framework import serializers
from .models import video_total_counts

class videosSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    videoId = serializers.IntegerField()
    dibsCount = serializers.IntegerField()
    watchCount= serializers.IntegerField()
    viewCount= serializers.IntegerField()

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return video_total_counts.objects.create(**validated_data)

    # Serializer.save()를 통해 DB 인스턴스를 수정 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 기존의 DB 인스턴스를 수정하고 반환
    def update(self, instance, validated_data):
        instance.dibsCount = validated_data.get('dibsCount', instance.dibsCount)
        instance.watchCount = validated_data.get('watchCount', instance.watchCount)
        instance.viewCount = validated_data.get('viewCount', instance.viewCount)
        instance.save()
        return instance

    class Meta:
        model = video_total_counts
        fields = ['videoId', 'dibsCount', 'watchCount', 'viewCount']
