from django.db import models

class Activity(models.Model):
    project_name = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)  # E.g., 'Task', 'Issue', etc.
    timestamp = models.DateTimeField(auto_now_add=True) 