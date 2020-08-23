from django import forms
from .models import *

class BlogForm(forms.ModelForm):
  pubdate = forms.DateTimeField(
    input_formats = ['%Y-%m-%dT%H:%M'],
    widget = forms.DateTimeInput(
      attrs={
        'type': 'datetime-local',
        'class': 'form-control'},
      format='%Y-%m-%dT%H:%M')
    )
  class Meta:
    model=Post
    fields =['title','author','pubdate','body'] 

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)