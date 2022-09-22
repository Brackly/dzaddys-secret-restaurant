from datetime import datetime
from django.shortcuts import redirect, render
from rest_framework.decorators import APIView,api_view
from .serializers import ReservationSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Reservation
from rest_framework.response import Response
import datetime
from django.db.models import Q

# Create your views here.
class getReservations(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'reservations.html'

    def get(self, request):
        reservations=Reservation.objects.all()
        return Response({'reservations': reservations})


def getReservation(request,id):
    reservation=Reservation.objects.get(id=id)
    return render(request,'reservation.html',{'reservation':reservation})
 
    
def createReservation(request):
    if request.method=='POST':
        print(request.POST)
        reservation=Reservation(
            reservation_date=request.POST['datepicker_field'],
            reservation_time=request.POST['time'],
            people=int(request.POST['people']),
            name=request.POST['name_reserve'],
            email=request.POST['email_reserve'],
            phone=request.POST['telephone_reserve'],
            additional_info=request.POST['opt_message_reserve'],
        )
        reservation.save()
        return render(request,'confirm.html')
    else:
        return render(request,'reservations.html')


def show_reservation(request,param):
    today=datetime.datetime.now().date()
    print(param)
    if(param==1):
        reservations=Reservation.objects.filter(reservation_date=today)
        title="Today's Reservations"
    elif(param==2):
        reservations=Reservation.objects.filter(reservation_date__gte=today)
        title="Future Reservations"
    elif(param==3):
        reservations=Reservation.objects.filter(reservation_date__lte=today)
        title="Previous Reservations"
    else:
        reservations=Reservation.objects.all()
        title="All Reservations"
    return render(request,'view_reservations.html',{'reservations':reservations,'title':title})

def clearReservation(request,id):
    reservation=Reservation.objects.get(id=id)
    reservation.cleared=True
    reservation.save()
    return redirect('reservation',id=id)
