from django import forms
from .models import Project, Position
from django.forms.models import inlineformset_factory

class CreateProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'timeline', 'requirements')

PositionFormSet = inlineformset_factory(
    Project, Position, form=CreateProject,
    fields=['position_title', 'position_description'], extra=4, can_delete=True
)
