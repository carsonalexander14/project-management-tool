from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]