from django import forms
from .models import ItemRent


class RentItemForm(forms.ModelForm):
    
    class Meta:
        model = ItemRent
        fields = '__all__'
    
    
    