from django.shortcuts import render
from django.http import HttpResponse,JsonResponse





def index_view(request):
    return HttpResponse('<h1>hi</h1>')



def about_view(request):
    return HttpResponse('<h1>Hello alii</h1>')



def contact_view(request):
    return HttpResponse('<h1>contact page</h1>')
