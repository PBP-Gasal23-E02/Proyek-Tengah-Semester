from django.shortcuts import get_object_or_404, redirect, render
from .models import Buku

def semua_buku(request):
    buku_bookmarked = Buku.objects.filter(bookmarked=True)
    buku_not_bookmarked = Buku.objects.filter(bookmarked=False)
    
    context = {
        'buku_bookmarked': buku_bookmarked,
        'buku_not_bookmarked': buku_not_bookmarked,
    }
    
    return render(request, 'semua_buku.html', context)

def all_bookmarked(request):
    bookmarked_book = Buku.objects.filter(bookmarked=True)
    return render(request, 'bookmarked_book.html', {'bookmarked_book': bookmarked_book})

def bookmark_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    buku.bookmarked = not buku.bookmarked
    buku.save()
    return redirect('detail_buku', buku_id=buku_id)

def add_bookmark(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    buku.bookmarked = True
    buku.save()
    return redirect('detail_buku', buku_id=buku_id)

def remove_bookmark(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    buku.bookmarked = False
    buku.save()
    return redirect('detail_buku', buku_id=buku_id)
