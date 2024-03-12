from django.http import HttpResponse
from django.shortcuts import render

from .models import Cards, CardsBig

    
def index(request):
    cards = Cards.objects.all()
    
    context = {'cards': cards,}
    
    return render(request, 'main/index.html', context)

def skills(request):
    return render(request, 'main/skills.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def project_page(request, project_slug):
    cards = Cards.objects.get(slug = project_slug)

    cards_big = CardsBig.objects.get(id = cards.id)    
    context = {
        'cards': cards,
        'cards_big': cards_big,
    }
    
    return render(request, 'main/project-page.html', context)
