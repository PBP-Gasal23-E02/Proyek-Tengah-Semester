from django.shortcuts import get_object_or_404, redirect, render
from .models import Buku
from bookmark.forms import BookmarkForm
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login/')
def show_main(request):
    Books = Buku.objects.all()

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
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_bookmark_json(request):
    bookmark_item = Buku.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', bookmark_item))

@csrf_exempt
def add_bookmark_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user

        new_bookmark = Buku(user=user, title=title, description=description)
        new_bookmark.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


