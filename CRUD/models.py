from django.db import models

class customerDetails(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name