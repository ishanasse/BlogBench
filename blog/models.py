from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    #author = models.CharField(max_length=30)
    # or
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title