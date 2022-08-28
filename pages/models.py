from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Issue(models.Model):
    TYPES_CHOICES = [
        ("Task", 'Task'),
        ("Bug", 'Bug'),
        ("Feature", 'Feature'),
      
    ]
   
    type = models.CharField(
        max_length=10,
        choices=TYPES_CHOICES,
        null=False,
    
    )

    description = models.TextField()

    STATUS_CHOICES = [
        ("In Progress", 'In Progress'),
        ("Closed", 'Closed'),
        ("Done", 'Done'),
    ]
    status = models.CharField(  
        max_length=100,
        choices=STATUS_CHOICES,
        null=False,)


