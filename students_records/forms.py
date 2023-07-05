from django import forms
from .models import Country, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'country']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


pass