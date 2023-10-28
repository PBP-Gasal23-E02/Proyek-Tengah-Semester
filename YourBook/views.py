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
from main.models import *
# Create your views here.
@login_required(login_url='login/')
def show_main(request):
    user = get_object_or_404(User, user=request.user)
    context = {
        'name': request.user.username,
        'class': user.user_type, 
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "pinjam.html", context)
def get_jumlah_item(request):

    jumlah_item = PinjamBuku.objects.filter(user=request.user).count()
    return JsonResponse({'jumlah_item': jumlah_item})

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

def get_product_json(request, filter):
    user = get_object_or_404(User, user=request.user)
    if user.user_type == "user":
        if filter == 'all':
            products = PinjamBuku.objects.filter(user=request.user)
        else:
            products = PinjamBuku.objects.filter(durasi_pinjam__lt=filter,user=request.user)
    else :
        if filter == 'all':
            products = PinjamBuku.objects.filter()
        else:
            products = PinjamBuku.objects.filter(durasi_pinjam__lt=filter)
    return HttpResponse(serializers.serialize('json', products))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        judul_buku = request.POST.get("judul")
        petugas = request.POST.get("petugas")
        durasi_pinjam = request.POST.get("durasi")
        catatan_peminjaman = request.POST.get("catatan")
        user = request.user

        # Coba untuk mencari buku dengan judul tertentu
        try:
            buku = Buku.objects.get(Title=judul_buku)
        except Buku.DoesNotExist:
            # Jika buku tidak ditemukan, kirim respons JSON
            return JsonResponse({'status': 'error', 'message': 'Buku tidak ditemukan'}, status=404)

        # Buat objek PinjamBuku
        new_product = PinjamBuku(
            buku=buku,
            user=user,
            judul_buku=judul_buku,
            petugas=petugas,
            durasi_pinjam=durasi_pinjam,
            catatan_peminjaman=catatan_peminjaman
        )
        new_product.save()

        return JsonResponse({'status': 'aman', 'message': 'Buku ditemukan'}, status=201)

    return JsonResponse({'status': 'error', 'message': 'Metode permintaan tidak valid'}, status=400)
    

def delete_item(request, id):
    item = get_object_or_404(PinjamBuku, id=id)
    item.delete()
    return JsonResponse({'message': 'Item berhasil dihapus.'})