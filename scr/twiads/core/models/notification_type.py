from django.db import models
from .base_model import BaseModel


class Notification_type(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'notification_types'