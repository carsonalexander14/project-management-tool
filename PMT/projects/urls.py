from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectList.as_view(), name='projects'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_details'),
]