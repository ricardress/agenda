from django.forms import ModelForm
from .models import Contacto

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        exclude = ('fecha',)
