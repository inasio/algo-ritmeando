from django import forms

class PostForm(forms.Form):
    url = forms.CharField(label = 'url de la imagen', max_length = 199)
    pwd = forms.CharField(widget=forms.PasswordInput(),label = 'contrasegna')