from django import forms
from django.forms import ModelForm
from .models import Tasks


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a new task title.'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Add the details of the task.'}))
    class Meta:
        model = Tasks
        fields = "__all__"