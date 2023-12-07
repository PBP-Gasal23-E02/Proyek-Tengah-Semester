import json
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from main.forms import ProductForm
from main.models import *
def show_awal(request):
    return render(request, "awal.html")

def show_main(request):
    form = ProductForm(request.POST or None)
    books = Buku.objects.all()
    context = {
        'books': books,
        'form': form,
        'name' : request.user.username,
    }
    return render(request, "main.html", context)

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login') 
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json",data), content_type= "application/json")

def get_books_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json",data))

def add_product_ajax(request):
    if request.method == 'POST':
        user_type = request.POST.get("role")
        user = request.user

        new_product = User(user=user,user_type=user_type)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_user(request):
    product_item = User.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def get_buku(request):
    product_item = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Buku.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)