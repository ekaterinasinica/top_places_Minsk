from django.shortcuts import render
from django.http import HttpResponse

from web.models import Card


def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})


def detail(request):
    return render(request, 'detail.html')
