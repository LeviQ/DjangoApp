from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(request, name):
    ls = ToDoList.objects.get(name = name)
    item = ls.item_set.get(id = 0)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))