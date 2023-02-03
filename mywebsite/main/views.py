from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def home(response):
    return render(response,'main/home.html',{})

def itemsList(response,name):
    list = ToDoList.objects.get(name=name)    
    return render(response,'main/items.html',{"list":list})

def itemDetails(response,id):
    return render(response, 'main/item_details.html',{"item":id})

def createItem(response):
    form = CreateNewList()
    return render(response,"main/create_item.html",{"form":form})

def lists(response):
    lists = ToDoList.objects.all()    
    return render(response,"main/lists.html",{"lists":lists})

def createList(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            list_name = form.cleaned_data["name"]
            new_list = ToDoList(name=list_name)
            new_list.save()
        return HttpResponseRedirect("/lists/")
    else:
        form = CreateNewList()
        return render(response,"main/create_list.html",{"form":form})