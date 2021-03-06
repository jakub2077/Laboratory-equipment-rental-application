from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
from django.views import generic
from django.contrib.auth.models import User

from .models import Item, ItemRent
from .forms import RentItemForm
from .api.permissons import _has_group_permission 

def home(request):
    """
    Home view
    """
    return render(request, 'items/home.html')

class ItemListView(PermissionRequiredMixin, LoginRequiredMixin, generic.list.ListView):
    """
    List all items in database
    """
    model = Item
    template_name = 'items/items_list.html'
    context_object_name = 'items'
    permission_required = 'items.view_item'

    def get_queryset(self):
        queryset = {
            'items': Item.objects.filter().all(),
            'teacher_permission': _has_group_permission(self.request.user, ['Teacher', 'admin'])
        }
        return queryset


class UserItemListView(ItemListView):
    """
    List items rented by request user
    """
    template_name = 'items/items_user.html'
    def get_queryset(self):
        queryset = {
            'items': Item.objects.filter(rented_by = self.request.user).all(),
            'rents': ItemRent.objects.filter(user_id = self.request.user).all(),
            'teacher_permission': _has_group_permission(self.request.user, ['Teacher', 'admin'])
        }
        return queryset


class ItemDetailView(PermissionRequiredMixin, LoginRequiredMixin, generic.DetailView):
    """
    Item details view
    """
    model = Item
    template_name = 'items/items_detail.html'
    permission_required = 'items.view_item'

    def get_object(self):
        item = Item.objects.filter(pk=self.kwargs['pk']).first()
        return item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher_permission"] = _has_group_permission(self.request.user, ['Teacher', 'admin'])
        return context
    

class ItemCreateView(PermissionRequiredMixin, LoginRequiredMixin, generic.CreateView):
    """
    Create a new Item instance
    """
    model = Item
    fields = [
        'university_number',
        'building_number',
        'faculty_number',
        'room_number',
        'item_number',
        'description',
        'status',
    ]
    template_name = 'items/items_create.html'
    queryset = Item.objects.all()
    permission_required = 'items.add_item'


class ItemUpdateView(PermissionRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Update Item instance
    """
    model = Item
    fields = '__all__'
    template_name = 'items/items_update.html'
    permission_required = 'items.change_item'

    def get_object(self):
        item = Item.objects.filter(pk=self.kwargs['pk']).first()
        return item

    def get_queryset(self):
        queryset = super(ItemUpdateView, self).get_queryset()
        return queryset.filter(user=self.request.user) 


class ItemRentListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """
    List all ItemRent instances (list of all rents)
    """
    model = ItemRent
    template_name = 'items/rents-list.html'
    context_object_name = 'rents'
    permission_required = 'items.view_itemrent'

    def get_queryset(self):
        queryset = {
            'active': ItemRent.objects.filter(is_archived=False).all(),
            'archived': ItemRent.objects.filter(is_archived=True).all(),
            'teacher_permission': _has_group_permission(self.request.user, ['Teacher', 'admin'])
        }
        return queryset


class ItemRentCreateView(LoginRequiredMixin, PermissionRequiredMixin ,generic.CreateView):
    """
    Create ItemRent instance
    """
    model = ItemRent
    template_name = 'items/rents-create.html'
    fields = [
        'item_id',
        'user_id',
        'rent_date',
        #'return_date',
    ]
    queryset = ItemRent.objects.all()
    permission_required = 'items.add_itemrent'


class ItemRentUpdateView(PermissionRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Update ItemRent instance
    """
    model = ItemRent
    fields = '__all__'
    template_name = 'items/rents-update.html'
    permission_required = 'items.change_itemrent'

    def get_object(self):
        object = ItemRent.objects.filter(pk=self.kwargs['pk']).first()
        return object

    def get_queryset(self):
        queryset = super(ItemRentUpdateView, self).get_queryset()
        return queryset.filter(user=self.request.user) 


# view for auto change item status and rented_by on creating ItemRent instance (Not working!)
def rent(request, item_id, user_id, date=timezone.now(), days=7):
    item = get_object_or_404(Item, id=item_id)
    user = get_object_or_404(User, id=user_id)
    if item.status == 'available':
        try:
            item_rent = ItemRent(item, user, date, timezone.timedelta(days=days))
            item_rent.save()
            item.status = 'rented'
            item.rented_by = user
            item.save()
        except:
            item_rent = ItemRent.objects.filter(item_id=item_id, user_id=user_id)
        
        context = {
            'item': item,
            'user_id': user,
            'rent': item_rent,
        }
        return render('items/rent.html', context)

    elif item.status == 'rented':
        messages.add_message(request, messages.WARNING, 'Item already rented')
    elif item.status == 'missing':
        messages.add_message(request, messages.WARNING, 'Item missing')
    else:
        messages.add_message(request, messages.WARNING, 'Error')


# testing forms
def createrent(request):
    form = RentItemForm(request.POST or None)         
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'items/rents-create.html', context)

