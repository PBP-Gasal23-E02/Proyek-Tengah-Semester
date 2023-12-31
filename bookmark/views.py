import json
from django.shortcuts import get_object_or_404, redirect, render
from .models import Bookmark
from bookmark.forms import BookmarkForm
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login/')
def show_main(request):
    Books = Bookmark.objects.all()

    context = {
        'books': Books,
        'name': request.user.username,
    }

    return render(request, "bookmark.html", context)

def add_bookmark(request):
    form = BookmarkForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        wishlist_item = form.save(commit=False)
        wishlist_item.user = request.user
        wishlist_item.save()
        return HttpResponseRedirect(reverse('bookmark:show_main'))

    context = {'form': form}
    return render(request, "add_bookmark.html", context)

def show_xml(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Bookmark.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Bookmark.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_bookmark_json(request):
    bookmark_item = Bookmark.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', bookmark_item))

@csrf_exempt
def add_bookmark_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user

        new_bookmark = Bookmark(title=title, description=description, user=user)
        new_bookmark.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def remove_bookmark(request, item_id):
    bookmark = Bookmark.objects.get(id = item_id)
    bookmark.delete()
    
    return HttpResponseRedirect(reverse('bookmark:show_main'))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Bookmark.objects.create(
            user = request.user,
            title = data["title"],
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
