from django import forms


class AddTweetForm(forms.Form):
    content = forms.CharField(label = 'Content', #will be displayed next to the form input field
                              max_length=400,
                              widget=forms.Textarea)
    tag = forms.CharField(label="Tag", required=False,)
