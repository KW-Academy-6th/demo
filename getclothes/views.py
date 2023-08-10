from django.shortcuts import render, redirect
from getclothes.models import GC

def home(request):
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
        temp_list.append(item.top)
        temp_list.append(item.bottom)
        temp_list.append(item.vehicle)
        temp_list.append(item.inout)
        values_list.append(temp_list)

    print(values_list)

    return render(request, 'list.html')

def recommend(request):
    return render(request, 'recommend.html')

def re_home(request):
    success = False

    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

        gc_obj = GC.objects.create(date=date, top=top, bottom=bottom, vehicle=vehicle, inout=inout)

        success = True

    return render(request, 're_home.html', {'success': success})

def list_edit(request):
    date = request.POST.get('date')
    rsDetail = GC.objects.filter(date=date)

    return render(request, "list_edit.html", {
        'rsDetail': rsDetail
    })

def update(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        top = request.POST.get('top')
        bottom = request.POST.get('bottom')
        vehicle = request.POST.get('vehicle')
        inout = request.POST.get('inout')

    try:
        gc = GC.objects.get(date=date)
        if top != "":
            gc.top = top
        if bottom != "":
            gc.b_note = bottom
        if vehicle != "":
            gc.vehicle = vehicle
        if inout != "":
            gc.inout = inout

        gc.save()
        return redirect('/list')
    except GC.DoesNotExist:
        # 원하는 날짜의 데이터가 없을 경우에 대한 처리
        pass

    return render(request, 'list_edit.html')