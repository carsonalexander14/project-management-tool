from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('create/', views.ProjectCreate.as_view(), name='project_create'),
    path('<slug:slug>/', login_required(views.ProjectDetail.as_view()), name='project_details'),
    path('<slug:slug>/edit', views.ProjectEdit.as_view(), name='project_edit'),
]