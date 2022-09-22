from django.urls import path,include
from .import views

urlpatterns=[
    path('',views.getMenuItems.as_view(),name="menu"),
    path('admin-dashboard/editmenu',views.getmenu,name="getmenu"),
    path('menu-of-the-day/',views.menu_of_the_day.as_view(),name="menu_of_the_day"),
    path('item/<int:id>/',views.getMenuItem.as_view(),name="MenuItem"),
    path('items/<str:params>/',views.filterMenu.as_view(),name="filterMenu"),
    path('admin-dashboard/create-menu-item/',views.createMenuItem,name="createmenuItem"),
    path('admin-dashboard/edit-menu-item/<int:id>',views.editmenuItem,name="editmenuItem"),
    path('admin-dashboard/delete-menu-item/<int:id>',views.deleteMenuItem,name="deleteMenuItem"),
    path('download/',views.downloadMenu,name="download-menu"),
]