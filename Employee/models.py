from django.db import models

# Create your models here.

class Employee(models.Model):
    Employee_id = models.IntegerField()
    Employee_name = models.CharField(max_length=30)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()
    Designation = models.CharField(max_length=50)
    Salary = models.IntegerField()
    Image = models.ImageField(upload_to='employee')

