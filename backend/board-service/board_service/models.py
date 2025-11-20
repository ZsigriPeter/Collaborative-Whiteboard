from django.db import models
from django.utils import timezone

class Board(models.Model):
    title=models.CharField(max_length=255)
    owner=models.IntegerField()
    
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    
    is_archived=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title