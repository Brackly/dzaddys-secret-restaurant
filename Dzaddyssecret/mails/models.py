from django.db import models

# Create your models here.

class EmailList(models.Model):
    email=models.EmailField()
    date=models.DateField(auto_now_add=True)
    read=models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Mail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    date=models.DateField(auto_now_add=True)
    read=models.BooleanField(default=False)

    def __str__(self):
        return ('Mail from {}'.format(self.email))
    