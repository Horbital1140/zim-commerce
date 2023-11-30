from django.http import HttpResponse
from django.shortcuts import render
from .models import product_details, funding


def index(request):
    MY_FOOD = product_details.objects.all()
    return render (request, 'index.html',
                   {'MY_FOOD' : MY_FOOD})



def news(request):
    fund = funding.objects.all()
    return render (request, 'news.html',
                   {'fund' : fund})
    


def sales(request):
    return HttpResponse('great sales today')



