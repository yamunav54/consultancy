from django.db import models

# Create your models here.

# DRY - Don't repeat yourself => Reusability

class Question(models.Model):
      qtext = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')


      def __str__(self):
         return self.qtext

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text