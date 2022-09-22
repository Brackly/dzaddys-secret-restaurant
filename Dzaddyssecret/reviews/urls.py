from django.urls import path
from .import views
urlpatterns=[
    path('',views.getReviews,name="reviews"),
    path('leave-review/',views.leave_review,name="leave_review"),

]