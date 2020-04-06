from django.db import models


class Task(models.Model):
    STATE_OPTIONS = [
        ('new', 'new'),
        ('inprogress', 'inprogress'),
        ('done', 'done'),
    ]
    title = models.CharField(max_length=202)
    description = models.TextField()
    state = models.CharField(max_length=20, choices=STATE_OPTIONS)