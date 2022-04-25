from tabnanny import verbose
from django.db import models



class Project(models.Model):
    pname=models.CharField(verbose_name='Project name', max_length=50)
    budget=models.FloatField(verbose_name='Budget value', null=True)

    def __str__(self):
        return self.pname

class Department(models.Model):
    dname=models.CharField(verbose_name='short name', max_length=5)
    description=models.CharField(verbose_name='Full name', max_length=100, null=True)


# Create your models here.
class Employee(models.Model):
    ename=models.CharField(verbose_name="Emp_name", max_length=50)
    joining_date=models.DateTimeField(verbose_name="Joining Date")
    Department=models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    project=models.ManyToManyField(Project,related_name='emp_project')
    created_date=models.DateTimeField(verbose_name="Record created on" ,auto_now_add=True)

    class Meta:
        verbose_name="Employee"
        verbose_name_plural="Employee"


    def __str__(self):
        x= (self.ename,str(self.joining_date))
        return " , ".join(x)
