from django.db import models

class Quesion(models.Model):
    question_text = models.CharField(max_lenght = 200)
    pub_date = models.DateTimeField('date published')
# Create your models here.
class Choice(models.Model):
    question = models.ForeignKey(Quesion,
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_lenght = 200)
    votes = models.IntegerField(default=0)
    
