from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login

from projects.views import ProjectList


class Home(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("signin"))
        return super().get(request, *args, **kwargs)


def redirect(request):
    if request.user.is_authenticated:
        return HttpResponsePermanentRedirect(reverse('projects:projects'))
    else:
        return HttpResponsePermanentRedirect(reverse('login'))
