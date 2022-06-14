from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    issued_date = models.DateField()
    submitted_date = models.DateField()
    
    


    def __str__(self):
        return self.name
