from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
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