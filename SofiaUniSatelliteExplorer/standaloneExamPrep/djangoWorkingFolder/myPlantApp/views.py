from django.shortcuts import render, redirect

from djangoWorkingFolder.myPlantApp.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from djangoWorkingFolder.myPlantApp.models import Plant, Profile


# Create your views here.

def getProfile():
    try:
        return Profile.objects.all().last()
    except:
        return None


def index(request):
    return render(request, 'home-page.html')


def createProfile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': True
    }
    return render(request, 'profile/create-profile.html', context)


def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }
    return render(request, 'plant/catalogue.html', context)


def createPlant(request):
    profile = getProfile()
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'plant/create-plant.html', context)


def plantDetails(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    user = getProfile()
    context = {
        'plant': plant,
        'user': user
    }
    return render(request, 'plant/plant-details.html', context)


def plantEdit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/edit-plant.html', context)


def plantDelete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = PlantDeleteForm(instance=plant)
    else:
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plant/delete-plant.html', context)


def profileDetails(request):
    profile = getProfile()
    plants = Plant.objects.all()
    context = {
        'profile': profile,
        'numberOfPlants': len(plants)
    }
    return render(request, 'profile/profile-details.html', context)


def profileEdit(request):
    profile = getProfile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form
    }
    return render(request, 'profile/edit-profile.html', context)


def profileDelete(request):
    profile = getProfile()
    if request.method == "POST":
        profile.delete()
        return redirect('catalogue')

    return render(request, 'profile/delete-profile.html')
