from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.username

class Profession(models.Model):
    name = models.CharField(max_length=60)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=40)
    create_date = models.DateTimeField()
    account = models.ForeignKey(Account)
    profession = models.ForeignKey(Profession)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name


