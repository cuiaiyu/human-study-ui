from django.db import models
from django.contrib.auth.models import User

MY_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
Q_TYPE_CHOICES = (
    ("single real/fake", "single real/fake"),
    ("real/fake", "real/fake"),
    ("conditional real/fake", "conditional real/fake"),
)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_ref_image = models.CharField(default='', max_length=200) 
    question_type = models.CharField(max_length=200, choices=Q_TYPE_CHOICES)
    correct_answer = models.CharField(max_length=1, choices=MY_CHOICES, default='C')

    def __str__(self):
        return self.question_text

    #def __init__(self):
    #    super(Question, self).__init__()
    #    self.choice_set.create(choice_text='A', votes=0)
    #    self.choice_set.create(choice_text='B', votes=0)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    query_image = models.CharField(default='', max_length=200) 
    choice_text = models.CharField(max_length=200, default='C')
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    user = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    choice = models.CharField(max_length=1, choices=MY_CHOICES)
    
    def __str__(self):
        return self.choice