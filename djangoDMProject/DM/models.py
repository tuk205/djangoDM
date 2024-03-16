from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    gold = models.IntegerField(default=0)
    hp = models.IntegerField(default=100)

    def __str__(self):
        return_name = str(self.player) + "`s inventory"
        return return_name


class ChangeLog(models.Model):
    version = models.CharField(max_length=10)
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.version

