from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    time = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=250)
    isDone = models.BooleanField()
    
