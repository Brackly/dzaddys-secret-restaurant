from django.urls import path,include
from .import views

urlpatterns=[
    path('',views.getReservations.as_view(),name="reservations"),
    path('<int:id>/',views.getReservation,name="reservation"),
    path('create-reservation/',views.createReservation,name="create-reservation"),
    path('show-reservations/<int:param>/',views.show_reservation,name="show-reservations"),
    path('clear-reservation/<int:id>/',views.clearReservation,name="clearReservation")


]