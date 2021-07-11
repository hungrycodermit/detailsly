from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class customerDetails(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, default="")
    Assignto = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.Assignto
