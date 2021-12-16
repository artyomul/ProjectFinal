from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vocab(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title