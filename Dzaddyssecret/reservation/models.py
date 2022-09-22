from django.db import models

# Create your models here.

class Reservation(models.Model):
    reservation_date=models.DateField()
    reservation_time=models.CharField(max_length=20)
    people=models.IntegerField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    additional_info=models.TextField(null=True,blank=True)
    cleared=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)


    #def __str__(self):
        #return 'Reservation for {} at {} on {}'.format(str(self.people),str(self.reservation_time),str(self.reservation_date))