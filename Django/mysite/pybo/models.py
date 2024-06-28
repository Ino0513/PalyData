from django.db import models

# Create your models here.
# Question 모델 -> subject, content, create_date
class Question(models.Model):
    subject = models.CharField(max_length= 200)
    content= models.TextField()
    create_date = models.DateTimeField()

# Answer 모델 -> question, content, create_date
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    # Answer 모델은 질문에 대한 답변 -> Question 모델을 속성으로 가져가야함
    # on_delete= models.CASCADE -> 연결된 Question이 사라지면 Answer도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()