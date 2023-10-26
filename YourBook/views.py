from django.shortcuts import render
from django.http import HttpResponseRedirect
from YourBook.forms import PinjamBukuForm
from django.urls import reverse
from YourBook.forms import PinjamBuku
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
    items = PinjamBuku.objects.filter(user=request.user)
    jumlah_item = PinjamBuku.objects.filter(user=request.user).count()

    context = {
        'name': request.user.username,
        'class': 'PBP E', 
        'items': items,
        'jumlah_item' : jumlah_item,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "pinjam.html", context)
def get_jumlah_item(request):
    # Logika untuk mendapatkan jumlah item (sesuai dengan kebutuhan Anda)
    jumlah_item = PinjamBuku.objects.filter(user=request.user).count()
    return JsonResponse({'jumlah_item': jumlah_item})

def create_product(request):
    form = PinjamBukuForm(request.POST or None)

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
    data = PinjamBuku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = PinjamBuku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = PinjamBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = PinjamBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def tambah_stok(request, id):
    item = get_object_or_404(PinjamBuku, id=id)
    if request.method == 'POST':
        # Tambah satu ke jumlah stok
        item.amount += 1
        item.save()
    return show_main(request)

def kurangi_stok(request, id):
    item = get_object_or_404(PinjamBuku, id=id)
    if request.method == 'POST':
        # Kurangi satu dari jumlah stok jika jumlah > 0
        if item.amount > 0:
            item.amount -= 1
            item.save()
    return show_main(request)

def hapus_item(request, id):
    item = get_object_or_404(PinjamBuku, id=id)
    if request.method == 'POST':
        item.delete()
    return show_main(request)

def edit_product(request, id):
    # Get product berdasarkan ID
    product = PinjamBuku.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = PinjamBukuForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('YourBook:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request, filter):
    if filter == 'all':
        products = PinjamBuku.objects.all()
    else:
        products = PinjamBuku.objects.filter(catatan_peminjaman__contains=filter)

    return HttpResponse(serializers.serialize('json', products))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        judul_buku = request.POST.get("judul")
        petugas = request.POST.get("petugas")
        durasi_pinjam = request.POST.get("durasi")
        catatan_peminjaman = request.POST.get("catatan")
        user = request.user

        new_product = PinjamBuku(user=user, petugas=petugas, judul_buku=judul_buku,durasi_pinjam=durasi_pinjam,catatan_peminjaman=catatan_peminjaman)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_item(request, id):
    item = get_object_or_404(PinjamBuku, id=id)
    item.delete()
    return JsonResponse({'message': 'Item berhasil dihapus.'})