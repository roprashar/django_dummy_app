from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# each class is transferred to the table in the database

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

