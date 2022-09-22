from django.shortcuts import render
from rest_framework.decorators import APIView,api_view
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.


def getReviews(request):
    reviews=Review.objects.all().order_by('date')

    for review in reviews:
        review.read=True
        review.save()
    overall_rating=0
    Total_rating=0
    count=1
    for review in reviews:
        Total_rating+=int(review.star)
        count+=1
    overall_rating=Total_rating/count
    return render(request,'showReviews.html',{'reviews': reviews,'overall_rating':overall_rating})


def leave_review(request):
    if request.method=='POST':
        #print(request.POST)
        review=Review(
            star= request.POST['rating-input'],
            title=request.POST['title'],
            body= request.POST['review']
        )
        #print(review)
        review.save()
        return render(request,'review_confirm.html')
    else:
        return render(request,'leave-review.html')