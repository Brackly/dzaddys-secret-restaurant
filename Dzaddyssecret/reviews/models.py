from django.db import models

# Create your models here.

stars=(
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5)
)

class Review(models.Model):
    star=models.CharField(max_length=120,choices=stars)
    title=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    date=models.DateField(auto_now_add=True)
    read=models.BooleanField(default=False)

    def __string__(self):
        return str(self.star)