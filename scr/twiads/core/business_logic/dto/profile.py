from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class EditProfileDto:
    username: str
    first_name: str
    last_name: str
    birth_date: date
    email: str
    bio: str
    country: Optional[str]



# class EditProfileForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     birth_date = forms.DateField(label="Birth Date")
#     email = forms.EmailField(label='Email')
#     bio = forms.CharField(required=False, max_length=50)
#     # avatar = forms.ImageField(label='Avatar')
#     following = ...
#     followers = ...
#     country = forms.ChoiceField(label='Country', choices=get_countries())