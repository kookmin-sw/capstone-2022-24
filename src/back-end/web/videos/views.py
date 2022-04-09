from typing_extensions import runtime
from rest_framework.pagination import PageNumberPagination #API랑 같이 페이징 할땐 이걸 쓰나봄...? 맞음?
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Videos, VideoDetails
from videos.serializer import VideosSerialaizer
from djongo.models import Q
from django.core.paginator import Paginator #페이징 용도
from django.views.generic import RedirectView, DetailView
from rest_framework.filters import SearchFilter

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.config.settings")
import django
django.setup()

from video_providers.models import VideoProviders


#Home 화면에서 video 목록을 보여주는 역할
class HomeView(ListAPIView):
    serializer_class = Videos #시리얼라이저 등록

    #모든 뷰 필터링 관련
    def get_queryset(self): #홈 화면에서 리스트를 전달해줄 함수.. 인데 얘가 곧 필터링/검색/정렬 기능을 포함해야함.

        queryset = Videos.object.all() #비디오 목록 전체

        #검색 조건
        search= self.request.query_params.get('search', None)
        if search is not None:
            queryset = Videos.object.filter(Q(title__icontains=search))

        #필터링 조건, 조건 안에서는 or처리, 조건 밖에서는 And 처리로 필터링한다.
        providers = self.request.query_params.get('providers', None)
        categories = self.request.query_params.get('categories', None)
        genres = self.request.query_params.get('genres', None)
        rating_min = self.request.query_params.get('ratingMin', None)
        rating_max = self.request.query_params.get('ratingMax', None)
        runtime_min = self.request.query_params.get('runtimeMin', None)
        runtime_max = self.request.query_params.get('runtimeMax', None)
        release_date_min = self.request.query_params.get('releaseDateMin', None)
        release_date_max = self.request.query_params.get('releaseDateMax', None)
        production_country= self.request.query_params.get('productionCountry', None)
        offer_type = self.request.query_params.get('offerTye', None)
        #watched = self.request.query_params.get('watched', None) 아직 미구현

        multiple_condition = [providers, genres, production_country, offer_type] #복수의 값이 들어올수 있는 애들 빼둠
        for item in multiple_condition: #복수로 들어왔는지 확인
            if item is not None:
                item = item.split(",")
            else:
                item = []

        if categories is not None:
            queryset= queryset.filter(Q(category=item))

        queryset = queryset.filter(Q(release_date__gt=release_date_min)&Q(release_date__It=release_date_max))

        for item in genres:
            queryset = queryset|queryset.filter(Q(gernes__icontains=[item]))

        #VideoDetail 모델을 참고해야하는 filtering
        subqueryset = VideoDetails.objects.all()
        subqueryset = subqueryset.filter(Q(runtime__gt=runtime_min)&Q(runtime__It=runtime_max))
        subqueryset = subqueryset.filter(Q(rating__gt=rating_min)&Q(rating__It=rating_max))
        for item in production_country:
            subqueryset = subqueryset|subqueryset.filter(Q(production_country=item))
        #아무튼 1차적으로 여기서 처리해서 And 연산해주기

        #video_providers 모델을 참고해야하는 filtering
        subqueryset= VideoProviders.objects.all()
        for item in providers:
            subqueryset= subqueryset|subqueryset.filter(Q(providers=item))
        for item in offer_type:
            subqueryset= subqueryset|subqueryset.filter(Q(offer_type=item))
        #아무튼 얘네 다 처리해준다음에 And 연산해주는것으로 filtering 종료.


        #정렬조건 { random | new | release | dib | star | rating }
        sort = self.request.query_params.get('sort', default='random')
        sort_dict= {'random':None, 'new':'offer_date', 'release':'release_date', 'dib': 'dibs_count', 'star': 'star_count', 'rating': 'rating'}
        try:
            if sort_dict[sort] == '': #new일때
                queryset= queryset.object.order_by(sort_dict[sort]) #이 친구는 video-> provider까지 가야해서 일단 따로 빼둠
            elif sort_dict[sort]=='': #random 이외.. 랜덤은 처리 아예 안할것임
                queryset= queryset.object.order_by(sort_dict[sort]) #정렬 기준에 맞춰서 정렬
        except: #대충 없는값을 전달 받았을 때
            pass


        #페이지네이션 정보
        page= self.kwargs['page']
        size = self.kwargs['size']

        #그다음에 페이지네이션 처리를 해서 전달한다.

        return queryset



class TvSeriesDirect(RedirectView): #그냥 시리즈 클릭하면 곧장 시즌 1로 리다이렉트 해주는 클래스
    url = '' #패턴...명을 지정해도 된다고 하네요?
    #아무튼 이걸 통해서 재리턴-> 재호출의 흐름을 거치게 할 예정입니다.


class DetailsView(DetailView): #각자 상세정보를 전달해줄 클래스 준비합니다.
    model= VideoDetails
    def MovieDetails(): # Movie 상세화면 정보를 전달해줄 클래스
        return 0

    def TVDetails(): #TV 상세화면 정보를 전달해줄 클래스
        return 0

    def castsDetails(): #casts 정보 따오기 (TV나 MOVIE나 동일하게 가도 될듯?)
        return 0
