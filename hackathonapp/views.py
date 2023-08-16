from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SingUpForm,UserForm
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from .weather import crawl_weather_data 
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ImageForm
from django.shortcuts import render
import os
from django.conf import settings
from .models import AwardImageUpload
from .models import ImageModel, AwardImageUpload


def weather_view(request):
# 크롤링한 데이터 가져오기
    temperature, humidity, personaltemp, third_element, UVdata3 = crawl_weather_data()

    # 템플릿에 데이터 전달
    context = {
        'temperature': temperature,
        'humidity': humidity,
        'personaltemp': personaltemp,
        'third_element': third_element,
        'UVdata3':UVdata3
    }

    return render(request, 'main.html', context)


# Create your views here.
def home(request):
    temperature, humidity, personaltemp, third_element, UVdata3, water, weather_icon, tshirts5, tshirts10, tshirts8, tshirts2 = crawl_weather_data()

    # 템플릿에 데이터 전달
    context = {
        'temperature': temperature,
        'humidity': humidity,
        'personaltemp': personaltemp,
        'third_element': third_element,
        'UVdata3':UVdata3,
        'water':water,
        'weather_icon':weather_icon,
        'tshirts5':tshirts5,
        'tshirts10':tshirts10,
        'tshirts8':tshirts8,
        'tshirts2':tshirts2,
    }

    return render(request, 'main.html', context)
    

def login(request):
    # 로그인 하고 나서 main페이지로 넘어가기
    return  render(request,'login.html')
def main(request):
    return  render(request,'main.html')


#signup2
def signup(request):
    # POST 요청인 경우에는 화면에서 입력한 데이터로 사용자를 생성하고 GET 요청인 경우에는 회원가입 화면을 보여준다.
    #데이터를 입력했을때
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()#입력된 데이터 저장
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            return redirect('home')
        else:#형식에 맞추지 않았을 때 다시 회원가입 기본화면
            return  render(request,'signup2.html')
    #get
    else:
        form = UserForm()
    return render(request, 'signup2.html', {'form': form})

def display_images(request):
    image_dir = os.path.join(settings.MEDIA_ROOT, 'images')
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]  # 이미지 확장자에 맞게 수정

    return render(request, 'display_images.html', {'image_files': image_files})

def about_me(request):

    award_image = AwardImageUpload.objects.all()

    return render(
        request,
        'templates/main.html',
        {
            'award_image': award_image
        }
    )

def display_image(request):
    # ImageModel에서 이미지 인스턴스 조회
    image_instance = ImageModel.objects.first()

    # AwardImageUpload에서 이미지 인스턴스 조회
    award_image_instance = AwardImageUpload.objects.first()

    return render(request, 'main.html', {
        'image_instance': image_instance,
        'award_image_instance': award_image_instance,
    })