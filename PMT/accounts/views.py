from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from accounts.forms import EditProfileForm
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from accounts.models import User 
from projects.models import Project, Position, Application

from django.urls import reverse_lazy
from django.views import generic

from . import forms


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


#profile 
@login_required
def profile(request):

    print(f'{request.user}: {request.user.id}')

    projects_list = Project.objects.filter(owner=request.user)

    context = {
        'user': request.user,
        'projects_list': projects_list,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def profile_edit(request):
    form = EditProfileForm(instance=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile')

    context = {
        'form': form
    }
    return render(request, 'accounts/profile_edit.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


