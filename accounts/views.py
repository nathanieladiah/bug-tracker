from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

# User = settings.AUTH_USER_MODEL
User = get_user_model()

# class SignUpView(CreateView):
# 	form_class = CustomUserCreationForm
# 	success_url = reverse_lazy('login')
# 	template_name = 'registration/signup.html'

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']

		# Ensure password matches confirmation
		password = request.POST['password']
		confirmation = request.POST['confirmation']

		if password != confirmation:
			return render(request, 'registration/register.html', {
				'message': 'Passwords must match.'
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, 'registration/register.html', {
				'message': 'Username already taken'
			})

		login(request, user)
		return HttpResponseRedirect(reverse('dashboard'))
	else:
		return render(request, 'registration/register.html')



# def login_view(request):
# 	if request.method == 'POST':
# 		# Attempt to sign user in
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		next_value = request.POST.get('next')
# 		print(next_value)

# 		# Check if authentication is successful
# 		if user is not None:
# 			login(request, user)
# 			if next_value == '':
# 				return HttpResponseRedirect(reverse('dashboard'))
# 			else:
# 				return redirect(next_value)
# 		else:
# 			return render(request, 'accounts/login.html', {
# 				'message': 'Invalid username and/or password.'
# 			})

# 	return render(request, 'accounts/login.html')


# def logout_view(request):
# 	logout(request)
# 	return HttpResponseRedirect(reverse('home'))
