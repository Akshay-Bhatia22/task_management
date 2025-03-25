from django.db import models
from django.utils import timezone
from Account.models import UserAccount

STATUS_OPTIONS = (("TO DO", 'To do'),
                ("IN PROGRESS", 'In Progress'),
                ("DONE", 'Done'),
                ("FAILED", 'Failed'),
                ("BACKLOG", 'Backlog'))

class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, related_name="created_tasks")
    task_type = models.CharField(max_length=100, null=True)
    completed_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS)
    assignee = models.ManyToManyField(UserAccount, related_name="assigned_tasks")

    def __str__(self):
        return self.name