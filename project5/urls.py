from django.contrib import admin
from django.urls import path
from mathserver import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bill),
]
