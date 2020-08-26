from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import UserManager, User, Skill


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "display_name", "bio", "avatar", "password1", "password2")
        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email Address"


class EditProfileForm(UserChangeForm):

    skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all())

    class Meta:
        fields = ("username", "display_name", "avatar", "bio", "skills")
        model = get_user_model()
