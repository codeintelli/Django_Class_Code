from django.db import models
from datetime import datetime
# Create your models here.

# after creating model you have to register the model in Home.admin.py


# makemigrations:- make migration and store in a file
# migrate:- apply the pending changes and created by makemigratio  and generate a file

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    message= models.TextField()
    date = models.DateField(blank=True,default=datetime(1111,11,11),null=True)


    def __str__(self):
        return self.name + "\t <" + self.email + ">"