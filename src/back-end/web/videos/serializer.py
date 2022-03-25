from rest_framework import serializers
from .models import videos, video_details

class videosSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    tmdbid = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    releaseDate= serializers.DateField()
    filmRating= serializers.CharField()
    category = serializers.CharField()
    posterKey = serializers.CharField()
    titleEnglish = serializers.CharField()

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return videos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tmdbid = validated_data.get('tmdbid', instance.tmdbid)
        instance.title = validated_data.get('title', instance.title)
        instance.releaseDate = validated_data.get('releaseDate', instance.releaseDate)
        instance.filmRating = validated_data.get('filmRating', instance.filmRating)
        instance.category= validated_data.get('category', instance.category)
        instance.posterKey= validated_data.get('posterKey', instance.posterKey)
        instance.titleEnglsih= validated_data.get('titleEnglish', instance.titleEnglish)
        instance.save()
        return instance

    class Meta:
        model = videos
        fields = ['tmdbid', 'title', 'code', 'releaseDate', 'filmRating', 'category', 'posterkey', 'titleEnglish']

class videosDetailsSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    runtime = serializers.IntegerField(null=False)
    releaseDate= serializers.DateField()
    rating = serializers.ListField(null=False)
    productionCountry= serializers.CharField(max_length=100, null=False)
    gernes= serializers.ListField(max_length=50, null=True)

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return video_details.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.runtime = validated_data.get('tmdbid', instance.runtime)
        instance.releaseDate = validated_data.get('title', instance.releaseDate)
        instance.rating = validated_data.get('releaseDate', instance.rating)
        instance.productionCountry = validated_data.get('filmRating', instance.productionCountry)
        instance.gernes= validated_data.get('category', instance.gernes)
        return instance

    class Meta:
        model = video_details
        fields = ['runtime', 'releaseDate', 'rating', 'productionCountry', 'gernes',]

