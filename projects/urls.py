from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
        path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),

        
        path('',views.projects, name="projects"),
        path('project/<str:pk>/',views.project, name="project"),

        path('create-project/', views.createProject, name="create-project"),
        path('update-project/<str:pk>/', views.updateProject, name="update-project"),
        path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),


]       