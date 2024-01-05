from django.urls import path

from djangoWorkingFolder.sofiauniproject.views import homeView, createView, mapDetails

urlpatterns = [
    path('', homeView, name='home view'),
    path('create/', createView, name='create view'),
    path('details/<int:pk>/', mapDetails, name='details view')
]
