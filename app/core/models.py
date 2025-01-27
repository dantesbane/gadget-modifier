from safedelete.models import SafeDeleteModel
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User

class Status(models.TextChoices):
    ACTIVE = 'Available'
    INACTIVE = 'Unavailable'
    DESTROYED = 'Destroyed'
    DECOMMISSIONED = 'Decommissioned'

class gadgets(models.Model):
    name = models.CharField(max_length=100,null=True)
    status=models.CharField(choices=Status.choices,null=False,default=Status.ACTIVE)


    def __str__(self):
        return self.name
    