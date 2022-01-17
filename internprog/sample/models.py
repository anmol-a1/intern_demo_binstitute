from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FilesAdmin(models.Model):
    title=models.CharField(max_length=50,unique=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='added+by+')