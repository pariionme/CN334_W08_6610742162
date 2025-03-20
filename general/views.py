from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce _index_view(request):
    '''This Function render index page of ecomerce views'''

    return HttpResponse('Welcome to CN334 Praewa 6610742162 views!')
