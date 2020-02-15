from django.db import models

# Create your models here.

class User(models.Model):
    first_Name = models.CharField(max_length=264)
    last_Name = models.CharField(max_length=264)
    user_email = models.CharField(max_length=150)

    def __str__(self):
        return self.first_Name + " " + self.last_Name