from .models import Homes
from django import forms

class HomesForm(forms.ModelForm):
    class Meta:
        model = Homes
        fields = ['names','email','number','message']