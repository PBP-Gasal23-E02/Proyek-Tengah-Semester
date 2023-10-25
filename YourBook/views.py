from django.shortcuts import render
from django.http import HttpResponseRedirect
from YourBook.forms import ItemForm
from django.urls import reverse
from YourBook.forms import Item
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

# Create your views here.
@login_required(login_url='login/')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    jumlah_item = Item.objects.filter(user=request.user).count()

    context = {
        'name': request.user.username,
        'class': 'PBP E', 
        'items': items,
        'jumlah_item' : jumlah_item,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "pinjam.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
     item = form.save(commit=False)
     item.user = request.user
     item.save()
     return HttpResponseRedirect(reverse('YourBook:show_main'))
    context = {
        'form' : form,
        }
    
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('YourBook:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("YourBook:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('YourBook:login'))
    response.delete_cookie('last_login')
    return response

def tambah_stok(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        # Tambah satu ke jumlah stok
        item.amount += 1
        item.save()
    return show_main(request)

def kurangi_stok(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        # Kurangi satu dari jumlah stok jika jumlah > 0
        if item.amount > 0:
            item.amount -= 1
            item.save()
    return show_main(request)

def hapus_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
    return show_main(request)

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('YourBook:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(user=user, name=name, amount=amount, description=description)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return JsonResponse({'message': 'Item berhasil dihapus.'})