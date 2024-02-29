from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddTeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['name'].empty_label='Введите имя'
    class Meta:
        model = Teacher
        fields = ['name', 'slug', 'brief_info', 'photo', 'add_info']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-input'}),
        }

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)>200:
            raise ValidationError('Длина превышает 200 символов')

        return name