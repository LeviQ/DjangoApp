from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [    
    path("",views.home,name="home"),        
    path("lists/",views.lists,name="lists"),
    path("list/create/",views.createList,name="create list"),
    path("list/<str:list_name>/",views.createItem,name="list items"),
    path("list/<str:name>/delete/",views.deleteList,name="delete list"),  
    path("list/<str:list_name>/<str:item_name>/delete/",views.deleteItem,name="delete lists item"),
    path("list/<str:list_name>/item/create/",views.createItem,name="create item")
]

urlpatterns += staticfiles_urlpatterns()