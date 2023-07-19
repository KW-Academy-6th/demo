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

def list_db(request):
    rsGC = GC.objects.all()

    values_list = []

    for item in rsGC:
        temp_list = []
        temp_list.append(item.date)
        temp_list.append(item.top)
        temp_list.append(item.bottom)
        temp_list.append(item.vehicle)
        temp_list.append(item.inout)
        values_list.append(temp_list)

    print(values_list)

    return render(request, 'list.html')