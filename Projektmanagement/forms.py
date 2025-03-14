from django import forms
from django.forms import fields

from .models import Task, User, Project


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'start_date', 'end_date', 'description', 'participants', 'project']

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

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                super().add_error('start_date', 'Start date cannot be after End date')

        return cleaned_data


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'done', 'start_date', 'end_date', 'description', 'participants', 'project']

    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, )

    start_date = fields.DateField(
        widget=DateInput,
        required=False, )

    end_date = fields.DateField(
        widget=DateInput,
        required=False, )

    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                super().add_error('start_date', 'Start date cannot be after End date')

        return cleaned_data
