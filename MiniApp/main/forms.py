from django import forms
from .models import User
from django.core.exceptions import ValidationError

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'patronymic', 'info', 'photo'}
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'patronymic': forms.TextInput(attrs={"class": "form-control"}),
            'info': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'photo': forms.FileInput(attrs={"class": "form-control", "rows": 5})
        }

