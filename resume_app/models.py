from django.db import models
from django.utils import timezone

# Create your models here.
class UserMessage(models.Model):
    subject = models.CharField(max_length=180)
    message = models.TextField()
    date_received = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
