from django.shortcuts import render
from .models import Mail,EmailList
# Create your views here.


def contact_us(request):
    if request.method=='POST':
        print(request.POST)
        mailing=Mail(
        name=request.POST['name_contact'],
        email=request.POST['email_contact'],
        message=request.POST['message_contact']
        )
        mailing.save()
        return render(request,'review_confirm.html')
    else:
        return render(request,'contacts.html')

def viewMails(request):
    mails=Mail.objects.all().order_by("date")
    for mail in mails:
        mail.read=True
        mail.save()
    return render(request,'Mails.html',{'mails':mails})

def viewMailingList(request):
    emails=EmailList.objects.all()
    for email in emails:
        email.read=True
        email.save()
    return render(request,'EmailList.html',{'emails':emails})