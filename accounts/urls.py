from django.urls import path

# from .views import SignUpView
from . import views

urlpatterns = [
	# path('signup/', SignUpView.as_view(), name='signup'),
	path('register/', views.register, name='signup'),
	path('logout/', views.logout_view, name='logout'),
	path('login/', views.login_view, name='login'),
]
