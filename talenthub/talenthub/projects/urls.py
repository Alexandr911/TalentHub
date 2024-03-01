from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<slug:project_slug>/', views.project, name="project"),
    # path('project-object/<str:pk>/', views.project, name="project"),
]