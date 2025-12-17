from django.db import models

# Create your models here.

class Emps(models.Model):
    # cnames=fields
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    salary=models.IntegerField()

    def  __str__(self):
        return self.name


# revise yesterday code once 
# all process of yesterday code