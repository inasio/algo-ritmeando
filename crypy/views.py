from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
    else:
        form = forms.PostForm()
    return render(request, 'index.html', {'form': form})
