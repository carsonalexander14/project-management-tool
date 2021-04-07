from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import F, Q
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from .forms import CreateProject, PositionFormSet
""" from projects.application_request_status import ApplicationRequestStatus
from projects.utils import get_application_request_or_false """
from projects.models import Project, Position, Application
"""  ApplicationList, ApplicationRequest """
from accounts.models import User, Skill

# Create your views here.

# OPEN LIST OF PROJECTS
class ProjectList(ListView):

    model = Project
    template_name = "project_list.html"
    context_object_name = "projects"
    paginate_by = 20   

    def get_queryset(self):
        position_val = self.request.GET.get('position','')
        if position_val == '':
            return Project.objects.all()
        else:
            projects = Project.objects.filter(position_set__position_title=position_val)
            return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['positions_list'] = Position.objects.all()
        return context

# PROJECT DETAILS
class ProjectDetail(DetailView):

    model = Project
    template_name = "project_details.html"
    context_object_name = "project_details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Project.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['now'] = timezone.now()
        context['skills_list'] = Skill.objects.all()
        return context

# CREATE PROJECT
class ProjectCreate(CreateView):
    
    model = Project
    form_class = CreateProject
    template_name = 'project_create.html'
    success_url = reverse_lazy('projects:projects')

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['position_formset'] = PositionFormSet(self.request.POST)
        else:
            context['position_formset'] = PositionFormSet()
        return context

    def form_valid(self, form):
        #CREATING CONTEXT
        context = self.get_context_data(form=form)
        #CREATING LINKING NAME FOR FORMSET
        formset = context['position_formset']
        #SETS PROJECT OWNER
        form.instance.owner = self.request.user
        #CREATES SAVE FOR FORMSET
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)

# EDIT PROJECT
class ProjectEdit(UpdateView):

    model = Project
    form_class = CreateProject
    template_name = 'project_edit.html'
    success_url = reverse_lazy('projects:projects')
    context_object_name = 'project_edit'

    def get_context_data(self, **kwargs):
        context = super(ProjectEdit, self).get_context_data(**kwargs)
        if self.request.POST:
            context['position_formset'] = PositionFormSet(self.request.POST, instance=self.object)
            context['position_formset'].full_clean()
        else:
            context['position_formset'] = PositionFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context['position_formset']
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)

# DELETE PROJECT
class ProjectDelete(DeleteView):

    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('projects:projects')
    context_object_name = 'project_delete'


# SEARCH PROJECTS BY TITLE AND DESCRIPTION
def search_projects(request):
    template_name = "project_list.html"

    query = request.GET.get('q')

    results = Project.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {'projects': results, }

    return render(request, template_name, context)


def application_apply(request):
    project_id = request.GET.get("project_id",'')
    position_id = request.GET.get("position_id",'')
    application = Application.objects.create()
    application.position = Position.objects.get(id=position_id)
    application.project = Project.objects.get(id=project_id)
    application.application_status = Application.PENDING
    application.applicant = User.objects.get(username = request.user.username)
    application.save()
    return HttpResponseRedirect(reverse('projects:applications_list'))


def application_accept(request):
    application_id = request.GET.get("application_id",'')
    application = Application.objects.get(id=application_id)
    application.application_status = Application.ACCEPTED
    application.save()
    return HttpResponseRedirect(reverse('projects:applications_list'))


def application_reject(request):
    application_id = request.GET.get("application_id",'')
    application = Application.objects.get(id=application_id)
    application.application_status = Application.REJECTED
    application.save()
    return HttpResponseRedirect(reverse('projects:applications_list'))


class ApplicationListView(ListView):

    model = Application
    template_name = "applications.html"

    def get_queryset(self):
        app_status = self.request.GET.get('application_status','P')
        applicant = self.request.user
        project_owner = self.request.user
        applicant_param = self.request.GET.get('applicant')
        powner_param = self.request.GET.get('project_owner')
        if (applicant_param == ''):
            app_list = Application.objects.filter(applicant=applicant, application_status=app_status)
            return app_list
        elif (powner_param == ''):
            app_list = Application.objects.filter(project__owner=project_owner, application_status=app_status)
            return app_list
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['projects_list'] = Project.objects.filter(owner=self.request.user)
        context['positions_list'] = Position.objects.filter(projects__owner=self.request.user)
        context['user_id'] = self.request.user.id
        application_status = self.request.GET.get('application_status', '')
        if application_status:
            context['application_list'] = Application.objects.filter(Q(applicant=self.request.user) | Q(project__owner=self.request.user) | Q(acceptor=self.request.user)).filter(application_status=self.request.GET.get('application_status','P'))
        else:
            context['application_list'] = Application.objects.filter(Q(applicant=self.request.user) | Q(project__owner=self.request.user) | Q(acceptor=self.request.user))
        return context

