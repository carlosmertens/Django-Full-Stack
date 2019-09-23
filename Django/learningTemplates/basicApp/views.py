from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'basicApp/index.html')


def page2(request):
    return render(request, 'basicApp/page2.html')


def relative(request):
    return render(request, 'basicApp/relative_url_templates.html')
