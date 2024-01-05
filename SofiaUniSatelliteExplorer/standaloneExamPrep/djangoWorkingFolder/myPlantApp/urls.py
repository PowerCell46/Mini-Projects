
"""
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page
"""

from django.urls import path, include

from djangoWorkingFolder.myPlantApp.views import index, createProfile, catalogue, createPlant, plantDetails, plantEdit, \
    plantDelete, profileDetails, profileEdit, profileDelete

urlpatterns = [
    path('', index, name='home page'),
    path('profile/create/', createProfile, name='create profile'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', createPlant, name='create plant'),
    path('details/<int:pk>/', plantDetails, name='plant details'),
    path('edit/<int:pk>/', plantEdit, name='plant edit'),
    path('delete/<int:pk>/', plantDelete, name='plant delete'),
    path('profile/', include([
        path('details/', profileDetails, name='profile details'),
        path('edit/', profileEdit, name='profile edit'),
        path('delete/', profileDelete, name='profile delete')
    ]))
]

# Relation between plants and users - every plant has to have a creator - on delete cascade
# Navigation needs to be fixed - profile and no profile cases
