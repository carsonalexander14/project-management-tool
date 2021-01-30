from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('create/', login_required(views.ProjectCreate.as_view()), name='project_create'),
    path('<slug:slug>/', login_required(views.ProjectDetail.as_view()), name='project_details'),
    path('<slug:slug>/edit', login_required(views.ProjectEdit.as_view()), name='project_edit'),
    path('<slug:slug>/delete', login_required(views.ProjectDelete.as_view()), name='project_delete'),
]