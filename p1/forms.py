from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import Questions


class QuestionsRegistration(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['Question_Text']