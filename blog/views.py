from django.http import HttpResponse
from django.shortcuts import render


def blog_views (request):
    return render (request,'blog/blog-home.html')



def blog_single (request):
    return render (request,'blog/blog-single.html')