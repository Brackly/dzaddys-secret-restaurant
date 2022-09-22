from django.http import HttpResponse,FileResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import APIView,api_view
from .serializers import MenuItemSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from .models import MenuItem
from rest_framework.response import Response
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import MenuItemForm
import mimetypes
import os

# Create your views here.

class getMenuItems(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu-1.html'

    def get(self, request):
        menuItems=MenuItem.objects.all()
        return Response({'MenuItems': menuItems})

class menu_of_the_day(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu-of-the-day.html'

    def get(self, request):
        menuItems=MenuItem.objects.all()
        return Response({'MenuItems': menuItems})


class getMenuItem(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu-1.html'

    def get(self, request,id):
        menuItem=MenuItem.objects.get(id=id)
        return Response({'menuItem': menuItem})

    def delete(self, request,id):
        menuItem=MenuItem.objects.get(id=id)
        menuItem.delete()
        return Response({'response': "Deleted"})

    def update(self, request,id):
        menuItem=MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(menuItem, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'menuItem': menuItem})
        serializer.save()



class filterMenu(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu-1.html'

    def get(self, request,params):
        menuItems=MenuItem.objects.filter(Q(food_type=params)|Q(categories=params))
        print(menuItems)
        return Response({'menuItems': menuItems})

def createMenuItem(request):
    if request.method=='POST':
        form=MenuItemForm(request.POST,request.FILES)
        valid=form.is_valid()
        if form.is_valid():
            form.save()
            return redirect('getmenu')
        else:
            err=form.errors
            return HttpResponse(err)     
    else:
        form=MenuItemForm()
        return render(request,'addMenuItem.html',{'form':form})
        

def getmenu(request):
    menuItems=MenuItem.objects.all()
    return render(request,'tables.html',{"menuItems":menuItems})

def editmenuItem(request,id):
    menuItem=MenuItem.objects.get(id=id)
    form=MenuItemForm(instance=menuItem)
    if request.method=='POST':
        form=MenuItemForm(request.POST,request.FILES,instance=menuItem)
        if form.is_valid():
            form.save()
            return redirect('getmenu')
    else:
        form=MenuItemForm(instance=menuItem)
        return render(request,'editMenuItem.html',{"form":form})

def deleteMenuItem(request,id):
    menuItem=MenuItem.objects.get(id=id)
    menuItem.delete()
    return redirect('getmenu')

def downloadMenu(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'menu.pdf'
    filepath = BASE_DIR + '/media/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response