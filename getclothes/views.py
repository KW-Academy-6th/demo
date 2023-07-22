from django.shortcuts import render, redirect
from getclothes.models import GC

def home(request):
    submit_count = request.session.get('submit_count', 0)
    success = False

    row_count = GC.get_row_count()
    if row_count >= 10:
        return redirect('recommend')

    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

        gc_obj = GC.objects.create(date=date, top=top, bottom=bottom, vehicle=vehicle, inout=inout)

        success = True

    return render(request, 'home.html', {'success': success})

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

def recommend(request):
    return render(request, 'recommend.html')
