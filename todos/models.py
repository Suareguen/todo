from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 20, null=False)
    status = models.BooleanField(default=False)
    text = models.TextField(max_length=100, null=True)
