from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

def home(response):
    return render(response,'main/home.html',{})

def itemsList(response):
    list = ToDoList.objects.get(id=3)    
    return render(response,'main/items.html',{"list":list})

def itemDetails(response,id):
    return render(response, 'main/item_details.html',{"item":id})

def createItem(response):
    form = CreateNewList()
    return render(response,"main/create_item.html",{"form":form})

def lists(response):
    return render(response,"main/lists.html",{})

def createList(response):
    return render(response,"main/create_list.html",{})