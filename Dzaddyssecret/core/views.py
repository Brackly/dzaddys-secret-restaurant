
from django.shortcuts import render
from django.views import View
from mails.models import EmailList

def home(request):
        return render(request,'index.html')
    
def contact_us(request):
    return render(request,'contacts.html')

def newsletter(request):
    if request.method=='POST':
        emaillist=EmailList(
            email=request.POST['email_newsletter']
        )
        emaillist.save()
        return render(request,'newsletter_confirm.html')

def gallery(request):
    return render(request,'404.html')