from django.db import models
from accounts.models import User


class Doc(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='docs')
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/')