from django.shortcuts import render, redirect

from djangoWorkingFolder.sofiauniproject.forms import SatelliteCreateForm
from djangoWorkingFolder.sofiauniproject.models import SatelliteImage


# Create your views here.


def homeView(request):
    context = {
        'satelliteData': SatelliteImage.objects.all().order_by('-publicationDate')
    }
    return render(request, 'home-page.html', context)


def createView(request):
    if request.method == "GET":
        form = SatelliteCreateForm()
    else:
        form = SatelliteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home view')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request, 'create-map.html', context)


def mapDetails(request, pk, map_type):
    context = {
        'satelliteData': SatelliteImage.objects.get(pk=pk),
        'map_type': map_type
    }
    return render(request, 'map-details.html', context)
