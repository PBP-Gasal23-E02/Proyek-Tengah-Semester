from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from wishlist.forms import WishlistBukuForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from wishlist.forms import WishlistBuku
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login/')
def show_main(request):
    first_login = request.user.date_joined
        
    wishlist_items = WishlistBuku.objects.filter(user=request.user)
    total_wishlist = len(wishlist_items)

    context = {
        'name': request.user.username,
        'wishlist_items' : wishlist_items,
        'total_wishlist' : total_wishlist,
        'user_login': first_login,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "wishlist.html", context)


def add_wishlist(request):
    title = request.GET.get('title', '')
    description = request.GET.get('description', '')

    # Create a form with the initial title and disable the 'title' field
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


@csrf_exempt
def edit_wishlist(request, id):
    wishlist = WishlistBuku.objects.get(pk = id)

    form = WishlistBukuForm(request.POST or None, instance=wishlist)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('wishlist:show_main'))

    context = {'form': form}
    return render(request, "edit_wishlist.html", context)

def remove_wishlist(request, item_id):
    wishlist = WishlistBuku.objects.get(id = item_id)
    wishlist.delete()
    
    return HttpResponseRedirect(reverse('wishlist:show_main'))

@csrf_exempt
def add_wishlist_ajax(request):
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

def get_wishlist_json(request):
    wishlist_item = WishlistBuku.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', wishlist_item))