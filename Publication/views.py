from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from Publication.forms import NewPublicationForm

def new_publication(request):
    form = NewPublicationForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        return HttpResponseRedirect(reverse('Publication:show_main'))
    
    context = {'form' : form}
    return render(request, "publication.html", context)
