from django.http import HttpResponse,JsonResponse


def index_views(request):
    return HttpResponse (' <h1>Home</h1>')

def about_views(request):
    return HttpResponse('<h1>About</h1>')


def contact_views(request):
    return HttpResponse(' <h1>Contact</h1>')
                                         