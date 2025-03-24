from django.db import models
from django.utils import timezone
from Account.models import UserAccount

STATUS_OPTIONS = (("TO DO", 'To do'),
                ("IN PROGRESS", 'In Progress'),
                ("DONE", 'Done'),
                ("FAILED", 'Failed'),
                ("BACKLOG", 'Backlog'))

class Task(models.Model):
#     2. Task: Represents a task in the system.
# - Fields: id, name, description, created_at, task_type, completed_at, status and other relevant
# fields.
# - A task can be assigned to multiple users, and a user can have multiple tasks.
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    task_type = models.CharField(max_length=100, null=True)
    completed_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS)
    assignee = models.ManyToManyField(UserAccount)
