"""woopolemong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    path('', views.index, name='index'),    # 포폴 게시판 메인페이지
    path('create/', views.create, name='create'),   # 게시글 생성
    path('<int:portfolio_pk>/', views.detail, name='detail'),   # 게시글 상세페이지
    path('<int:portfolio_pk>/update/', views.update, name='update'),   # 게시글 수정
    path('<int:portfolio_pk>/delete/', views.delete, name='delete'),   # 게시글 삭제
    path('portfoliolist/', views.projectlist, name='projectlist'),   # 프로젝트 리스트
    path('image/<int:image_pk>/delete/', views.image_delete, name='image_delete'),  # 이미지 삭제
]
