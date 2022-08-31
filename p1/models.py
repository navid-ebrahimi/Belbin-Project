from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    estimated_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Questions(models.Model):
    Question_Text = models.CharField(max_length=500, null=True)
    Test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='question')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Question_Text


class Options(models.Model):
    Option_Text = models.TextField()
    Question = models.ForeignKey(Questions, on_delete=models.CASCADE,related_name='option')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Option_Text} , {self.Question.Question_Text}"

class Answers(models.Model):
    number = models.IntegerField()
    Option = models.ForeignKey(Options, on_delete=models.CASCADE, related_name='answer')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} , {self.Option} , {self.number}"