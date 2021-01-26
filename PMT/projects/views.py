from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.utils import timezone
from django.http import HttpResponse

from projects.utils import get_application_request_or_false
from projects.models import Project, Position, ApplicationList, ApplicationRequest
from accounts.models import User 

# Create your views here.

#view for open list of projects. like the "home" of projects
class ProjectList(ListView):

    model = Project
    template_name = "projects.html"
    context_object_name = "projects"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

#view for details of projects. Singular projects details.
class ProjectDetail(DetailView):

    model = Project
    template_name = "project_details.html"
    context_object_name = "project_details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Project.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['now'] = timezone.now()
        return context

@login_required
def application_list_view(request, ApplicationList, ApplicationRequest):
    try:
        application_list = ApplicationList.objects.get(user=acceptor)
    except ApplicationList.DoesNotExist:
        application_list = ApplicationList(user=acceptor)
        application_list.save()
    applications = application_list.applications.all()
    context = {'applications': applications}
    is_self = True
    is_acceptor = False
    user = request.user

    if applications.filter(pk=user.id):
        is_acceptor = True
    else:
        is_acceptor = False
        if get_application_request_or_false(sender=acceptor, receiver=user) != False:
            request_sent = ApplicationRequestStatus.THEM_SENT_TO_YOU.value
            context['pending_application_request_id'] = get_application_request_or_false(sender=acceptor, receiver=user).id
        elif get_application_request_or_false(sender=acceptor, receiver=user) != False:
            request_sent = ApplicationRequestStatus.YOU_SENT_TO_THEM.value
        else:
            request_sent = ApplicationRequestStatus.NO_REQUEST_SENT.value
            
    try:
        application_requests = ApplicationRequest.objects.filter(receiver=user, is_active=True)
    except:
        pass

    context = {'is_self': is_self}
    context = {'is_acceptor': is_acceptor}
    context = {'request_sent': request_sent}
    context = {'friend_requests': friend_requests}
    return context
