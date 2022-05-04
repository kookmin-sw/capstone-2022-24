"""Admin : TvSeriesDetail, TvSeason, TvSeasonDetail"""
from django.contrib import admin
from tv_details.models import TvSeason, TvSeasonDetail, TvSeriesDetail

admin.site.register(TvSeriesDetail)
admin.site.register(TvSeason)
admin.site.register(TvSeasonDetail)
