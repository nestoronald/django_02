from django import forms
from models import Articulos
class ArticulosForm(forms.ModelForm):
 
   class Meta:
      model = Articulos
