from django.db import models
from django.contrib.auth.models import User

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Sprint(models.Model):
    name = models.CharField(  
        max_length=100,
        )


class Issue(models.Model):

    sprint = models.ForeignKey(Sprint, 
    on_delete=models.CASCADE,
    related_name="issues",
    null=True,)

    user = models.ForeignKey(User, 
    on_delete=models.CASCADE,
    related_name="issues",
    null=True,)
   

    TYPES_CHOICES = [
        ("", ''), 
        ("Task", 'Task'),
        ("Bug", 'Bug'),
        ("Feature", 'Feature'),
    ]
   
    type = models.CharField(
        max_length=10,
        choices=TYPES_CHOICES,
        null=True,
    
    )

    description = models.TextField()

    STATUS_CHOICES = [
        ("", ''), 
        ("In Progress", 'In Progress'),
        ("Closed", 'Closed'),
        ("Done", 'Done'),
    ]
    status = models.CharField(  
        max_length=100,
        choices=STATUS_CHOICES,
        null=True ,)




