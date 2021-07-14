from django import forms
from .models import Dog

# Create your forms here.

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'sex', 'breed', 'is_neutered', 'weight']

