from django.http import HttpResponse
from django.shortcuts import render


def index_views(request):
    return render (request,'website/index.html')

def about_views(request):
    return render(request,'website/about.html')


def contact_views(request):
    return render(request,'website/contact.html')


def test_views(request):
    return render(request,'website/test.html',{'name':'mhmd','lastname':'babaie'})

                                         