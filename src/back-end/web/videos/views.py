from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import videos, video_details
from videos.serializer import videosSerialaizer


# Create your views here.
def videoListing(): #video 홈화면에서 리스트를 전달해줄 클래스
    print('hi')

def videoSearch(request): #video 홈화면에서 검색을 해줄 클래스 아래 있는건 걍 예시문 하나 따온거임.. 참고만 하자
    content_list = videos.objects.all()
    search = request.GET.get('search','')
    if search:
        search_list = content_list.filter(
        #Q(title__icontains = search) | #제목
        #Q(body__icontains = search) | #내용
        #Q(writer__username__icontains = search) #글쓴이
        )
    #paginator = Paginator(search_list,5)
    page = request.GET.get('page','')
    #posts = paginator.get_page(page)
    #board = Board.objects.all()

    return render(request, 'search.html',{'posts':'posts', 'Board':'board', 'search':search})

def MovieDetails(): #Movie 상세화면 정보를 전달해줄 클래스
    return 0

def TVDetails(): #TV 상세화면 정보를 전달해줄 클래스
    return 0

def castsDetails(): #casts 정보 따오기 (TV나 MOVIE나 동일하게 가도 될듯?)
    return 0