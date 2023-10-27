from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from review.forms import ReviewForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from review.forms import ReviewBuku
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')

def show_main(request):
    products = ReviewBuku.objects.filter(user=request.user)
    context = {
        'user': request.user.username,
        'book': 'test',
        'products': products,
    }

    return render(request, "show_review.html", context)

def create_product(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('review:show_main'))

    context = {'form': form}
    return render(request, "write_review.html", context)

def show_xml(request):
    data = ReviewBuku.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ReviewBuku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ReviewBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ReviewBuku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    products = ReviewBuku.objects.filter(user=request.user)
    product_list = []
    for product in products:
        product_dict = {
            'pk': product.pk,
            'book': product.book,
            'review_cust': product.review_cust,
           
        }
        product_list.append(product_dict)
    return JsonResponse(product_list, safe=False)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponse("Created", status=201)
        else:
            # Handle form validation errors and return as JSON
            errors = form.errors.as_json()
            return HttpResponseBadRequest(errors, content_type='application/json')

    return HttpResponseNotFound()