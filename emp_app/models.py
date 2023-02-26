from django.db import models

# Create your models here.
class Department(models.Model):
    Dep_name = models.CharField(max_length = 200, null=False,)
    location = models.CharField(max_length = 200,)

    def __str__(self):
        return "%s %s" %(self.Dep_name, self.location)

class Role(models.Model):
    role_name = models.CharField(max_length = 200, null=False)

    def __str__(self):  
        return  self.role_name

class Employee(models.Model):
    first_name = models.CharField(max_length = 200, null=False, blank=False)
    last_name = models.CharField(max_length = 200,)
    email = models.EmailField(max_length = 500, null=False,)
    dept = models.ForeignKey(Department, on_delete= models.CASCADE)
    sal  = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete= models.CASCADE)
    hire_date = models.DateTimeField()

    def __str__(self):
        return "%s %s %s %s %s" %(self.first_name, self.last_name, self.email, self.hire_date, self.sal)
