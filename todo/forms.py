from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        exclude =('fecha',)
        widgets={
            'fechaFinalizacion':DateInput(attrs={'type': 'Date'}),
        }
