from django.db import models

# Create your models here.

category_choices=(
    ('Drink','Drink'),
    ('Food','Food')
)

type_choices=(
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Main','Main')
)

class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField()
    categories=models.CharField(max_length=120,choices=category_choices)
    food_type=models.CharField(max_length=120,choices=type_choices)
    def __str__(self):
        return str(self.name)