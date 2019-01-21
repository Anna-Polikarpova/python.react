from django.shortcuts import render, get_object_or_404

from .models import Item


# Create your views here.
def list(request):
    items = Item.objects.all()
    return render(request, 'main/list.html', {'items': items})


def detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'main/detail.html', {'item': item})
