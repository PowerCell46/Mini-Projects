from django.shortcuts import render

# Create your views here.


def homeView(request):
     return render(request, 'home-page.html')


def createView(request):
    if request.method == "GET":
        return render(request, 'create-map.html')


def mapDetails(request, pk):
    print(pk)
    return render(request, 'map-details.html')
