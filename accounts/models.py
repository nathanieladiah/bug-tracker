from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
	ROLE_CHOICES = [
		('admin', 'Administrator'),
		('manager', 'Project Manger'),
		('dev', 'Developer')
	]

	role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='dev')
	# profile_pic


	def __str__(self):
		return self.username
