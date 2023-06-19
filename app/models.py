from django.db import models

# Create your models here.

class Dept(models.Model):
    DEPT_NO=models.DecimalField(max_digits=3,decimal_places=1,primary_key=True)
    DNAME=models.CharField(max_length=30)
    LOC=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.DNAME

class Emp(models.Model):
    EMPNO=models.DecimalField(max_digits=5,decimal_places=1)
    ENAME=models.CharField(max_length=50)
    JOB=models.CharField(max_length=50)
    MGR=models.DecimalField(max_digits=5,decimal_places=1)
    HIRE_DATE=models.DateField()
    SAL=models.DecimalField(max_digits=7,decimal_places=2)
    COMM=models.DecimalField(max_digits=6,decimal_places=1)
    DEPT_NO=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ENAME