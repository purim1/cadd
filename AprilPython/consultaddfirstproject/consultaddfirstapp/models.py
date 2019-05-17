from django.db import models

# Create your models here.

class Candidate(models.Model):
    Name_of_Can=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.Name_of_Can


class CandidateInfo(models.Model):
    CanID=models.ForeignKey(Candidate,on_delete=models.PROTECT)
    CandDept = models.CharField(max_length=150,unique=True)


class CandidateAddress(models.Model):
    CanAddr = models.CharField(max_length=150,unique=True)


class CandidateSalary(models.Model):
    CanSalary = models.CharField(max_length=150,unique=True)

