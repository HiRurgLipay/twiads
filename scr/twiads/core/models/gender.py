from django.db import models
from .base_model import BaseModel


class Gender(BaseModel):
    name = models.CharField(max_length=50, 
                            unique=True)
    
    class Meta:
        db_table = 'genders'
        