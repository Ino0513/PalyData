# mysite/pybo/urls
from django.urls import path
from . import views

app_name = 'pybo' # namespace 중복 방지를 위해 선언

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:question_id>', views.detail, name= 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]