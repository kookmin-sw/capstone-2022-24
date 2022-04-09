from rest_framework import serializers
from .models import videos, video_details

class VideosSerialaizer(serializers.Serializer):
    # 시리얼라이즈/디시리얼라이즈 되어야 하는 모델 필드들
    tmdb_id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    release_Date= serializers.DateField()
    film_rating= serializers.CharField()
    category = serializers.CharField()
    poster_key = serializers.ImageField()
    title_english = serializers.CharField()

    # Serializer.save()를 통해 DB 인스턴스를 생성할 때의 동작 정의
    # 유효성 검사를 통과한 데이터들을 바탕으로 새로운 DB 인스턴스를 생성하고 반환
    def create(self, validated_data):
        return videos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tmdb_id = validated_data.get('tmdbid', instance.tmdb_id)
        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get('releaseDate', instance.release_date)
        instance.film_rating = validated_data.get('filmRating', instance.film_rating)
        instance.category= validated_data.get('category', instance.category)
        instance.poster_key= validated_data.get('posterKey', instance.poster_key)
        instance.title_english= validated_data.get('titleEnglish', instance.title_english)
        instance.save()
        return instance

    class Meta:
        model = videos
        fields = ['tmdb_id', 'title', 'release_date', 'film_rating', 'category', 'poster_key', 'title_english']

class VideosDetailsSerialaizer(serializers.Serializer):
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
