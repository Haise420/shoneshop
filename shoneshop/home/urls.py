from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('izbrisi-proizvod/<int:proizvod_id>', views.delete_proizvod, name="delete_proizvod")
]