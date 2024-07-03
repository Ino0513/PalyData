# mysite/pybo/forms.py

from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    # ModelForm을 상속
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 모델의 속성

        # 폼 레이블 추가
        labels = {
            'subject': '제목',
            'content': '내용',
        }