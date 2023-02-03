from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [    
    path("",views.home,name="home"),    
    path("items/<int:id>/",views.itemDetails,name="item details"),
    path("items/create/",views.createItem,name="create item"),
    path("lists/",views.lists,name="lists"),
    path("list/create/",views.createList,name="create list"),
    path("list/<str:name>/",views.itemsList,name="list items"),
    path("list/<str:name>/delete",views.deleteList,name="delete List")
]

urlpatterns += staticfiles_urlpatterns()