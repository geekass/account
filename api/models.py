from django.db import models
from django_extensions.db.fields import UUIDField


class User(models.Model):
    id = UUIDField(version=4, primary_key=True, auto_created=True)
    full_name = models.CharField(max_length=255, default=None)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    sign_up_date = models.DateTimeField(auto_now_add=True)
