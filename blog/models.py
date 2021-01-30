from django.db import models
from datetime import datetime

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title