from django.urls import path

from . import views

urlpatterns = [    
    path("",views.home,name="home"),
    path("items/",views.itemsList,name="items list"),
    path("items/<int:id>/",views.itemDetails,name="item details"),
    path("items/create/",views.createItem,name="create item"),
    path("lists/",views.lists,name="lists"),
    path("lists/create/",views.createList,name="create list")
]