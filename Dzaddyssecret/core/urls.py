
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',include('mails.urls')),
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('menu/',include('menuItem.urls')),
    path('reservations/',include('reservation.urls')),
    path('reviews/',include('reviews.urls')),
    path('newsletter/',views.newsletter, name="newsletter"),
    path('gallery/',views.gallery, name="gallery"),
    path('accounts/', include('allauth.urls')),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)