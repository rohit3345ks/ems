from django.db import models

# Create your models here.

class employee(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    employeeID = models.AutoField(primary_key=True)
    city=models.CharField(max_length=20)

def __str__(self):
    return self.title