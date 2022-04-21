"""Serializers of star_ratings application for json parsing"""
from rest_framework import serializers


class StarRatingSerializer(serializers.ModelSerializer):
    """Serializer of StarRating Model"""
