from django.db import models
from django.contrib.auth.models import AbstractUser
from model.baseModel import BaseModel


class User(AbstractUser,BaseModel):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    age = models.CharField(max_length=3,blank=True)
    username = models.CharField(max_length=255, blank=True, unique=True)
    email = models.CharField(max_length=255, blank=True,unique=True)
    password = models.CharField(max_length=255, blank=True)




    USERNAME_FIELD = ["username"]


    def __str__(self) -> str:
        return str(id)
    


    class Meta:
        db_table = "Users"
        indexes = [
            models.Index(fields=['first_name', 'last_name',"username","email"])
        ]