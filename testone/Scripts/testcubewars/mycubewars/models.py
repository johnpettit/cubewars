from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.username