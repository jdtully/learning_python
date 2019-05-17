
from django.shortcuts import render
from .models import BibleVerse
from django.http import HttpResponse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'fullbible_app/index.html'
    context_object_name = 'bible_verse'

    def get_queryset(self):
        return BibleVerse.objects.order_by('?').first()