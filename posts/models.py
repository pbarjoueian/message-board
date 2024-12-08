from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.TextField(null=False, unique=True)

    def __str__(self):
        return f"{self.id}: {self.text}"
