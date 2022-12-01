from django.db import models

# Create your models here.


class Emp(models.Model):
    name = models.CharField(max_length=230)
    address = models.CharField(max_length=230)



class Course(models.Model):
    name = models.CharField(max_length=230)
    dis = models.CharField(max_length=230)


    