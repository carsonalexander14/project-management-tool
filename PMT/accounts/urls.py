from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>', views.profile, name='profile'),
]