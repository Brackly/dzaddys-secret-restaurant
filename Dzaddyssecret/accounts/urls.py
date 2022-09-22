
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin-dashboard',views.admin_dashboard,name="admin-dashboard")

]