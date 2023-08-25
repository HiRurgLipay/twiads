from django import forms

class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birth_date = forms.DateField(label="Birth Date")
    email = forms.EmailField(label='Email')
    # avatar = forms.ImageField(label='Avatar')
    following = ...
    followers = ...
    country = forms.CharField(label='Country', max_length=100)

# Также у него должна быть возможность отредактировать свой профиль: 
# поменять фотограцию, юзернейм, имейл, имя, фамилию, дату рождения, краткое описание своего профиля, страну.