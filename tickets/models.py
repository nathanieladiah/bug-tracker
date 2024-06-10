from django.conf import settings
from django.db import models


class Change(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	property = models.CharField(max_length=200)
	old_value = models.CharField(max_length=200)
	new_value = models.CharField(max_length=200)
	time = models.DateTimeField(auto_now=True)
	ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} - {self.property}'

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	content = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.user} - {self.time}'

class Project(models.Model):
	manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	# many to many - assigned devs?
	title = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title

class Ticket(models.Model):

	STATUS_CHOICES = [
		('open', 'Open'),
		('in_progress', 'In Progress'),
		('closed', 'Closed'),
	]

	TYPE_CHOICES = [
        ('bugs', 'Bugs/Errors'),
        ('features', 'Feature Request'),
        ('docs', 'Training/Documentation Required'),
        ('other', 'Other'),
	]

	title = models.CharField(max_length=200)
	description = models.TextField()
	project = models.ForeignKey('Project', on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
	type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='bugs')
	assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	# files

	def __str__(self):
		return self.title
