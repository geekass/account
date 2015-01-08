from django.db import models
from django_extensions.db.fields import UUIDField


class UserExtras(models.Model):
    id = UUIDField(version=4, primary_key=True)
    email = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
