from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from publication.forms import NewPublicationForm
from publication.models import Book

@login_required(login_url='login/')
def show_main(request):
    books = Book.objects.filter(user=request.user)
    
    context = {
        'account': request.user.username,
        'book': books,
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