from django.db import models

# Create your models here.

 
class register_table(models.Model):
    username = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)  # Use this name
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username














