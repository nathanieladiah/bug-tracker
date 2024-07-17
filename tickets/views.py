from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Project


@login_required
def dashboard(request):
	return render(request, 'tickets/dashboard.html')

class ProjectsListView(ListView):
	model = Project

class ProjectDetailView(DetailView):
	model = Project
