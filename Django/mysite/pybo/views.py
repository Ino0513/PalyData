# mysite/pybo/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date') # 생성 날짜순으로 질문 목록을 정렬
    context = {'question_list': question_list}

    return render(request, 'pybo/question_list.html', context) # render()는 파이썬 데이터를 템플릿에 적용해 html로 변환, render 함수가 리턴한 question_list.html과 같은 파일을 템플릿 이라고 부름

# 질문 상세 기능
def detail(request, question_id):
    question = get_object_or_404(id= question_id)
    context = {'question' : question}

    return render(request, 'pybo/question_detail.html', context)

# 답변 생성 기능
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    question.answer_set.create(content= request.POST.get('content'), create_date= timezone.now()) # 텍스트 창에서 입력한 내용으로 Answer모델을 생성

    # 답변을 생성한 후 화면을 다시 보여주기 위해 redirect
    return redirect('pybo:detail', question_id= question.id)