from django import forms
from .models import Student_informations

class RegistForm(forms.ModelForm,forms.Form):
    class Meta:
        model = Student_informations
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Father': forms.TextInput(attrs={'class': 'form-control'}),
            'Grand_Father': forms.TextInput(attrs={'class': 'form-control'}),
            'Date_of_Birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Place_of_Birth': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    
