from django import forms
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        exclude = ["user", "completed_at"]


# GET and POST are the only 2 methods that work with forms.
