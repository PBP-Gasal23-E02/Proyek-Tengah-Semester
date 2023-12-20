from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from publication.forms import NewPublicationForm
from publication.models import Publication
from main.models import Buku
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='login/')
def show_main(request):
    books = Publication.objects.filter(user=request.user)
    
    context = {
        'account': request.user.username,
        'books': books,
    }
    return render(request, "your_publication.html", context)

def new_publication(request):
    form = NewPublicationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        # Ambil data dari formulir
        author = form.cleaned_data['author']
        title = form.cleaned_data['title']
        subjects = form.cleaned_data['subjects']
        language = form.cleaned_data['language']
        bookshelves = form.cleaned_data['bookshelves']
        locc = form.cleaned_data['locc']

        # Simpan objek Buku terlebih dahulu
        book = Buku.objects.create(
            Authors=author,
            Title=title,
            Subjects=subjects,
            Language=language,
            # Issued=issued,
            Bookshelves=bookshelves,
            LoCC=locc
        )

        with open('main/fixtures/books.json', 'r') as file:
            dataset = json.load(file)

        dataset.append({
            "pk": book.pk,
            "model": "main.buku",
            "fields": {
                "Text": "-",
                "Type": "Text",
                "Issued": book.Issued,
                "Title": book.Title,
                "Language": book.Language,
                "Authors": book.Authors,
                "Subjects": book.Subjects,
                "LoCC": "TX",
                "Bookshelves": "Cookbooks and Cooking",
            }
        })
        
        with open('main/fixtures/books.json', 'w') as file:
                json.dump(dataset, file, indent=4)

        buku = form.save(commit=False)
        buku.user = request.user
        buku.save()
        return HttpResponseRedirect(reverse('publication:show_main'))
    
    context = {'form' : form}
    return render(request, "publication.html", context)

@csrf_exempt
def new_publication_ajax(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        title = request.POST.get("title")
        subjects = request.POST.get("subjects")
        language = request.POST.get("language")
        bookshelves = request.POST.get("bookshelves")
        locc = request.POST.get("locc")
        user = request.user

        # Simpan objek Buku terlebih dahulu
        book = Publication.objects.create(
            user=user,
            author=author,
            title=title,
            subjects=subjects,
            language=language,
            bookshelves=bookshelves,
            locc=locc
        )

        with open('main/fixtures/books.json', 'r') as file:
            dataset = json.load(file)

        dataset.append({
            "pk": book.pk,
            "model": "main.buku",
            "fields": {
                "Text": "-",
                "Type": "Text",
                "Issued": book.Issued,
                "Title": book.Title,
                "Language": book.Language,
                "Authors": book.Authors,
                "Subjects": book.Subjects,
                "LoCC": book.locc,
                "Bookshelves": book.bookshelves,
            }
        })

        with open('main/fixtures/books.json', 'w') as file:
            json.dump(dataset, file, indent=4)

        # book = Publication(user = user, author = author, title = title, subjects = subjects, language = language, bookshelves = bookshelves, locc = locc)
        book.save()

        return HttpResponse(b"CREATED", status=201)
    
    # Mengembalikan respons JSON dengan status gagal jika permintaan bukan metode POST atau formulir tidak valid
    return HttpResponseNotFound()

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

@csrf_exempt
def get_buku_user(request):
    product_item = Publication.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def new_publication_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        book = Publication.objects.create(
            user = request.user,
            author=data["author"],
            title=data["title"],
            subjects=data["subjects"],
            language=data["language"],
            issued=data["issued"],
            bookshelves=data["bookshelves"],
            locc=data["locc"],
        )

        with open('main/fixtures/books.json', 'r') as file:
            dataset = json.load(file)

        dataset.append({
            "pk": book.pk,
            "model": "main.buku",
            "fields": {
                "Text": "-",
                "Type": "Text",
                "Issued": book.issued,
                "Title": book.title,
                "Language": book.language,
                "Authors": book.author,
                "Subjects": book.subjects,
                "LoCC": book.locc,
                "Bookshelves": book.bookshelves,
            }
        })
        
        with open('main/fixtures/books.json', 'w') as file:
                json.dump(dataset, file, indent=4)

        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
# temp