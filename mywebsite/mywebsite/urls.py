from django.contrib import admin
from django.urls import include, path
from main import views

urlpatterns = [
    #path('polls/', include('main.urls')),
    path('admin/', admin.site.urls),
    path("<str:name>", views.index, name='index'),
]