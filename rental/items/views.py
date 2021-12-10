from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Item

@login_required
def list_items(request):
    data = {
        'items': Item.objects.all(),
    }
    return render(request, 'items/list_items.html', data)

@login_required
def view_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    data = {
        'item': item,
    }
    return render(request, 'items/view_item.html', data)

def home(request):
    return render(request, 'items/home.html')