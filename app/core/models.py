from safedelete.models import SafeDeleteModel
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User

class Status(models.TextChoices):
    ACTIVE = 'Available'
    INACTIVE = 'Unavailable'
    DESTROYED = 'Destroyed'
    DECOMMISSIONED = 'Decommissioned'

class gadgets(models.Model):
    name = models.CharField(max_length=100)
    status=models.Enum

    def __str__(self):
        return self.name
    