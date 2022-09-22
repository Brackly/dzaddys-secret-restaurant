from django.forms import ModelForm,TextInput, EmailInput,ImageField,Select
from .models import MenuItem

class MenuItemForm(ModelForm):
    class Meta:
        model=MenuItem
        fields='__all__'
        