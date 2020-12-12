from django.forms import ModelForm
from .models import Menu
from django import forms

"""
class MenuForm(forms.Form):
    Fecha_Menu = forms.DateField(label = 'Fecha del menú')
    Op_1 = forms.CharField(label = 'Opción 1 del menú', max_length=200)
    Op_2 = forms.CharField(label = 'Opción 2 del menú', max_length=200)
    Op_3 = forms.CharField(label = 'Opción 3 del menú', max_length=200)
    Op_4 = forms.CharField(label = 'Opción 4 del menú', max_length=200)
"""

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['Fecha', 'Opcion_1', 'Opcion_2', 'Opcion_3', 'Opcion_4']

"""
class OpcionForm(ModelForm):
    class Meta:
        model = Opcion
        fields = ['Num_Opcion', 'Plato_Fondo', 'Ensalada', 'Postre']
"""