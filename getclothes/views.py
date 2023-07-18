from django.shortcuts import render, redirect
from getclothes.models import GC

def home(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

        gc_obj = GC.objects.create(date=date, top=top, bottom=bottom, vehicle=vehicle, inout=inout)

        success = True

        return render(request, 'home.html', {'success':success})

    return render(request, 'home.html')

def list(request):
    rsGC = GC.objects.all()

    return render(request, 'list.html', {
        'rsGC': rsGC
    })