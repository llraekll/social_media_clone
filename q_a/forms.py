from .models import Answer
from django import forms

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['name', 'content']

        widgets = {                                             
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # A widget is Django’s representation of an HTML input element. The widget handles the rendering of the HTML, 
        # and the extraction of data from a GET/POST dictionary that corresponds to the widget.
