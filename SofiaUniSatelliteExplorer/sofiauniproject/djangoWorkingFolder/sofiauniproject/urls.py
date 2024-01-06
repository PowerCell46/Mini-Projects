from django.urls import path

from djangoWorkingFolder.sofiauniproject.views import homeView, createView, mapDetails

urlpatterns = [
    path('', homeView, name='home view'),
    path('create/', createView, name='create view'),
    path('details/true-colour/<int:pk>/', mapDetails, {'map_type': 'true-colour'}, name='true colour details view'),
    path('details/false-colour/<int:pk>/', mapDetails, {'map_type': 'false-colour'}, name='false colour details view'),
    path('details/ndvi/<int:pk>', mapDetails, {'map_type': 'ndvi'}, name='ndvi details view')
]
