import json
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from wishlist.forms import WishlistBukuForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from wishlist.forms import WishlistBuku
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from main.models import *
from django.contrib import messages
from django.contrib.auth import logout


@login_required(login_url='login/')
def show_main(request):
    try:
        user = User.objects.get(user=request.user)
        first_login = request.user.date_joined
        wishlist_items = WishlistBuku.objects.filter(user=request.user)
        total_wishlist = len(wishlist_items)
        role = user.user_type

        context = {
            'name': request.user.username,
            'wishlist_items': wishlist_items,
            'total_wishlist': total_wishlist,
            'user_login': first_login,
            'role': role,
            'last_login': request.COOKIES.get('last_login', ''),
        }

        return render(request, "wishlist.html", context)

    except User.DoesNotExist:
        return render(request, "main.html")


def add_wishlist(request):
    title = request.GET.get('title', '')
    description = request.GET.get('description', '')

    form = WishlistBukuForm(initial={'title': title, 'description': description})
    form.fields['title'].widget.attrs['readonly'] = True

    if request.method == "POST":
        form = WishlistBukuForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.save()
            return HttpResponseRedirect(reverse('wishlist:show_main'))

    context = {'form': form}
    return render(request, "add_wishlist.html", context)

def remove_wishlist(request, item_id):
    wishlist = WishlistBuku.objects.get(id = item_id)
    wishlist.delete()
    
    return HttpResponseRedirect(reverse('wishlist:show_main'))

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@csrf_exempt
def add_wishlist_ajax(request):
    user = get_object_or_404(User, user=request.user)
    if (user.user_type == "user"):
        messages.warning(request, "Anda tidak memiliki izin untuk mengakses halaman ini.")
    else :
        if request.method == 'POST':
            title = request.POST.get("title")
            description = request.POST.get("description")
            user = request.user

            new_wishlist = WishlistBuku(title=title, description=description, user=user)
            new_wishlist.save()

            response_data = {'message': 'Item added to wishlist'}
            return JsonResponse(response_data, status=201)

    return HttpResponseNotFound()

def show_xml(request):
    data = WishlistBuku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WishlistBuku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WishlistBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = WishlistBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def get_wishlist_json(request):
    wishlist_item = WishlistBuku.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', wishlist_item))

@csrf_exempt
def create_wishlist_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_wishlist = WishlistBuku.objects.create(
            user = request.user,
            title = data["title"],
            description = data["description"],
        )

        new_wishlist.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_wishlist_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        wishlist_book = get_object_or_404(WishlistBuku, id=data['id'])
        wishlist_book.delete()
        return JsonResponse({"status": True,}, status=200)
    
    return JsonResponse({"status": False}, status=500)