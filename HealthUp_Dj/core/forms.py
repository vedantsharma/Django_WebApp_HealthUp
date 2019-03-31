from django import forms

from .models import Prescription

class PresForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('title', 'patient', 'pdf', 'cover')