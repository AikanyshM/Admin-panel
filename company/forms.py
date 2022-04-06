from django import forms
from .models import Apartment, Block

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        
class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'