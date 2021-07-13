from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
class Follower(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    follower_id = models.ManyToManyField(User, related_name="flower")

class Following(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    following_id = models.ManyToManyField(User, related_name="flowing")
