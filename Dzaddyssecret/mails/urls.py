
from django.urls import path
from .import views

urlpatterns = [
    path('contact-us/',views.contact_us,name="contact_us"),
    path('admin/dashboard/mails/',views.viewMails,name="mails"),
    path('admin/dashboard/email-list/',views.viewMailingList,name="EmailList")

]