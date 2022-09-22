from django.shortcuts import render
from reservation.models import Reservation
from reviews.models import Review
from mails.models import Mail,EmailList
from itertools import chain
from django.contrib.auth.models import User

# Create your views here.



def admin_dashboard(request):
    if request.user.is_staff==True:
        reservations=Reservation.objects.filter(cleared=False).order_by("date").count()
        reviews=Review.objects.filter(read=False).order_by("date").count()
        mails=Mail.objects.filter(read=False).order_by("date").count()
        emails=EmailList.objects.filter(read=False).order_by("date").count()

        return render(request,'dashboard_content.html',{
            'reviews':reviews,
            'reservations':reservations,
            'mails':mails,
            'emails':emails})
    else:
       return render(request,'404.html')