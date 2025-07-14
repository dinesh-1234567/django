from django.db import models

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="No description provided.")
    due_date = models.DateField(default='2025-12-31')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
