from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from publication.forms import NewPublicationForm
from publication.models import Publication

@login_required(login_url='login/')
def show_main(request):
    books = Publication.objects.filter(user=request.user)
    books_count = len(books)
    
    context = {
        'account': request.user.username,
        'book': books,
        'books_count': books_count
    }
    return render(request, "your_publication.html", context)

def new_publication(request):
    form = NewPublicationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return HttpResponseRedirect(reverse('publication:show_main'))
    
    context = {'form' : form}
    return render(request, "publication.html", context)

def show_xml(request):
    data = Publication.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Publication.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Publication.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Publication.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")