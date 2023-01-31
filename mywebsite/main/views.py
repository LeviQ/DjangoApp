from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def other(response, name):
    ls = ToDoList.objects.get(name = name)
    item = ls.item_set.get(id = 0)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

def home(response):
    return render(response,'main/base.html',{})

def itemsList(response):
    return HttpResponse("<h1>Items List</h1>")

def itemDetails(response,id):
    return HttpResponse(f"<h1>Item Details: {id}</h1>")