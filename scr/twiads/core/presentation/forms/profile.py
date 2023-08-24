from django import forms

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    registration_date =  ...
    email = forms.EmailField(label='Email')
    # avatar = forms.ImageField(label='Avatar')
    following = ...
    followers = ...
    country = forms.CharField(label='Country', max_length=100)
