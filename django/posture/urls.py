from unicodedata import name
from django.urls import path

from . import views

app_name = 'posture'


urlpatterns = [
    # 메인페이지 "{% url 'posture:main' %}"
    path('', views.index, name='main'), 

    # 마이페이지 "{% url 'posture:mypage' %}"
    path('mypage/', views.mypage, name='mypage'),

    # 마이페이지 수정 "{% url 'posture:mypage_modify' %}"
    path('mypage_modify/', views.mypage_modify, name='mypage_modify'),

    # 회원가입 "{% url 'posture:signup' %}"
    path('signup/', views.signup, name='signup'),

    
]