from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = '__all__' # list of fields you want from model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('title',css_class='form-group col-md-6 mb-0'),
                Column('author', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'body',
            Submit('submit', '確認', css_class='form-group col-md-6 mb-0')
        )