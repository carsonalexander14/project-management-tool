from django import forms
from .models import Project

class CreateProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'timeline', 'requirements')

        