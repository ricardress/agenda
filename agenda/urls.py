
from django.contrib import admin
from django.urls import include, path
from agenda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', include('contacto.urls')),
    path('todo/', include('todo.urls')),
    path('', views.index, name='index'),
]
