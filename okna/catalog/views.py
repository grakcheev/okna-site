from django.shortcuts import get_object_or_404, render

from .models import Item


def index(request):
    items = Item.objects.all()

    return render(request, 'catalog/index.html', context={'items': items, })
