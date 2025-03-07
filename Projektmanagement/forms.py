from django import forms
from django.forms import fields, DateTimeInput, DateInput

from .models import Task, User, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'description', 'participants', 'project']

    class DateInput(forms.DateInput):
        input_type = 'date'

    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    start_date = fields.DateTimeField(
        widget=DateInput,
        required=False,
    )

    end_date = fields.DateTimeField(
        widget=DateInput,
        required=False,
    )
