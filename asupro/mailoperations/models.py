from django.db import models

# Create your models here.
class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=30,)