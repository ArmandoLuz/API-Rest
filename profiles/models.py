from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self) -> str:
        return self.username