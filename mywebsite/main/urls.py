from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [    
    path("",views.home,name="home"),
    path("items/",views.itemsList,name="items list"),
    path("items/<int:id>/",views.itemDetails,name="item details"),
    path("items/create/",views.createItem,name="create item"),
    path("lists/",views.lists,name="lists"),
    path("list/create/",views.createList,name="create list")
]

urlpatterns += staticfiles_urlpatterns()