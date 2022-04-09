from rest_framework import serializers
from .models import video_total_counts

class videosSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    video_id = serializers.IntegerField()
    dibs_count = serializers.IntegerField()
    watch_count= serializers.IntegerField()
    view_count= serializers.IntegerField()

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return video_total_counts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dibs_count = validated_data.get(
            'dibs_count',
            instance.dibs_count,
        )
        instance.watch_count = validated_data.get(
            'watch_count',
            instance.watch_count
        )
        instance.viewCount = validated_data.get(
            'view_count',
            instance.view_count
        )
        instance.save()
        return instance

    class Meta:
        model = video_total_counts
        fields = ['videoId', 'dibsCount', 'watchCount', 'viewCount']
