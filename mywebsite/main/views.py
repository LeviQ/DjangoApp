from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList,CreateNewItemForList

def home(response):
    return render(response,'main/home.html',{})

def createItem(response,list_name):
    list = ToDoList.objects.get(name=list_name)
    if response.method == "POST":
        form = CreateNewItemForList(response.POST)
        if form.is_valid():
            item_name = form.cleaned_data["name"]
            item_description = form.cleaned_data["description"]
            item_completed = form.cleaned_data["completed"]

            #sprawdzenie czy istnieje już item o takiej nazwie
            try:
                searched = list.item_set.get(text=item_name)
            except Item.DoesNotExist:
                list.item_set.create(text=item_name,description=item_description,complete=item_completed)
            finally:
                searched = None
                
            return HttpResponseRedirect(f"/list/{list.name}/")
    else:
        form = CreateNewItemForList()
        return render(response,'main/items.html',{"list":list,"form":form})

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

def deleteList(response, name):
    list = ToDoList.objects.get(name = name)
    list.delete()
    lists = ToDoList.objects.all()
    return render(response,'main/lists.html',{"lists":lists})

def deleteItem(response,list_name,item_name):
    list = ToDoList.objects.get(name=list_name)
    item = list.item_set.get(text=item_name)
    item.delete()

    return HttpResponseRedirect(f"/list/{list.name}/")
        

