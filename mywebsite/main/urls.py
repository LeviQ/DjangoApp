from django.urls import path

from . import views

urlpatterns = [    
    path("",views.home,name="home"),
    path("items/",views.itemsList,name="items list"),
    path("items/<int:id>/",views.itemDetails,name="item details"),
    #path("<str:name>", views.index, name='index'),
]