django-admin startproject gas_utility_service
cd gas_utility_service
django-admin startapp customer_service

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Submitted', 'Submitted'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved')
    ], default='Submitted')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
