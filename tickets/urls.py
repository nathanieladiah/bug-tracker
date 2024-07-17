from django.urls import path

from .views import ProjectDetailView, ProjectsListView, dashboard

urlpatterns = [
	path('dashboard/', dashboard, name='dashboard'),
	path('projects/', ProjectsListView.as_view(), name='projects'),
	path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
]
