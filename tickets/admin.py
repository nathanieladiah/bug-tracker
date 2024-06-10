from django.contrib import admin

from .models import Change, Comment, Project, Ticket


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
	list_display = ('ticket', 'user', 'property', 'old_value', 'new_value', 'time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'ticket', 'time')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'manager')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('title', 'project', 'status', 'type')
