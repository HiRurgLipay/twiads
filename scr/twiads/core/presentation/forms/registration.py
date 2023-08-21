from django import forms
from core.models import Country

USER_COUNTRY_CHOICES = [(country.name, country.name) for country in Country.objects.all()]

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Enter password: ", widget=forms.PasswordInput, max_length=128)
    email = forms.EmailField(label="Enter email: ")
    first_name = forms.CharField(label="First Name", max_length=150)
    last_name = forms.CharField(label="Last Name", max_length=150)
    birth_date = forms.DateField(label="Birth Date")
    country = forms.ChoiceField(label="Country", choices=USER_COUNTRY_CHOICES)
