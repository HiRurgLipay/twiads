from django import forms
from core.models import Country

def get_countries() -> list:
    USER_COUNTRY_CHOICES = [(country.name, country.name) for country in Country.objects.all()]
    return USER_COUNTRY_CHOICES

class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birth_date = forms.DateField(label="Birth Date")
    email = forms.EmailField(label='Email')
    bio = forms.CharField(required=False, max_length=50)
    # avatar = forms.ImageField(label='Avatar')
    following = ...
    followers = ...
    country = forms.ChoiceField(label='Country', choices=get_countries())

# Также у него должна быть возможность отредактировать свой профиль: 
# поменять фотограцию, юзернейм, имейл, имя, фамилию, дату рождения, краткое описание своего профиля, страну.