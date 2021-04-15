from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('results/', login_required(views.search_projects), name='search'),
    path('create/', login_required(views.ProjectCreate.as_view()), name='project_create'),
    path('applications/', login_required(views.ApplicationListView.as_view()), name='applications_list'),
    path('applications/apply', login_required(views.application_apply), name='application_apply'),
    path('applications/accept', login_required(views.application_accept), name='application_accept'),
    path('applications/reject', login_required(views.application_reject), name='application_reject'),
    path('applications/notificationsread', login_required(views.mark_all_as_read), name='mark_all_as_read'),
    # path('dailypointschart/', views.daily_points, name='dailypointschart'),
    path('<slug:slug>/', login_required(views.ProjectDetail.as_view()), name='project_details'),
    path('<slug:slug>/edit', login_required(views.ProjectEdit.as_view()), name='project_edit'),
    path('<slug:slug>/delete', login_required(views.ProjectDelete.as_view()), name='project_delete'),
]