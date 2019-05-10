from django.shortcuts import render
from .models import BibleVerse

from django.http import HttpResponse

def home(request):
    verse=BibleVerse.objects.order_by('?').first().verse
    return HttpResponse(verse)
