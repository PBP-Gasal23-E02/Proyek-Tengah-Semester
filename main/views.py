from django.shortcuts import render

def show_main(request):
    context = {
        'kelompok': 'E02'
    }

    return render(request, "main.html", context)
