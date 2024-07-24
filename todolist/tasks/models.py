from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Task"  # Singular name

    def __str__(self):
        return self.title
