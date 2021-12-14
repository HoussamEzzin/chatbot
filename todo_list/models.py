from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

''' 

id
title
content
color
date
'''

class Todo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    color = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title
    