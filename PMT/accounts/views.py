from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

from . import forms

#login, logout, signup

# class LoginView(generic.FormView):
    #form_class = AuthenticationForm
    #success_url = reverse_lazy("PMT:home")
    #template_name = "accounts/signin.html"
    
    #def get_form(self, form_class=None):
        #if form_class is None:
            #form_class = self.get_form_class()
        #return form_class(self.request, **self.get_form_kwargs())
    
    #def form_valid(self, form):
        #login(self.request, form.get_user())
        #return super().form_valid(form)


#class LogoutView(generic.RedirectView):
    #url = reverse_lazy("home")
    
    #def get(self, request, *args, **kwargs):
        #logout(request)
        #return super().get(request, *args, **kwargs)


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

#profile 
@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/profile_edit.html', args)





