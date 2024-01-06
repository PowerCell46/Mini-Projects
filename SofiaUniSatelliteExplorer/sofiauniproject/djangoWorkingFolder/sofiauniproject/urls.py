from django.urls import path
from django.conf import  settings
from djangoWorkingFolder.sofiauniproject.views import homeView, createView, mapDetails
from django.conf.urls.static import static

urlpatterns = [
    path('', homeView, name='home view'),
    path('create/', createView, name='create view'),
    path('details/true-colour/<int:pk>/', mapDetails, {'map_type': 'true-colour'}, name='true colour details view'),
    path('details/false-colour/<int:pk>/', mapDetails, {'map_type': 'false-colour'}, name='false colour details view'),
    path('details/ndvi/<int:pk>', mapDetails, {'map_type': 'ndvi'}, name='ndvi details view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
