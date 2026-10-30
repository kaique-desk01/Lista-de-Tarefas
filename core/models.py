from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title