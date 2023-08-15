from django.contrib.auth.models import AbstractUser
from django.db import models

from .base_model import BaseModel


class User(BaseModel, AbstractUser):
    """User model which we add"""

    birth_date = models.DateField()
    avatar = models.ImageField(upload_to="", null=True)
    subscribers_count = models.PositiveIntegerField(default=0)
    subscriptions_count = models.PositiveIntegerField(default=0)
    tweets_count = models.PositiveIntegerField(default=0)

    subscriber = models.ManyToManyField(
        to="self",  # link to self
        symmetrical=False,  # relation are not symmetrical
        related_name="subscriptions",  # name to feedback
        db_table="subscriber_user",
    )
    gender = models.ForeignKey(to="Gender", on_delete=models.CASCADE, related_name="users")
    country = models.ForeignKey(to="Country", on_delete=models.CASCADE, related_name="users")

    class Meta:
        """Rename"""

        db_table = "users"
