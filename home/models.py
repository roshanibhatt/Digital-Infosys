from django.db import models


# Create your models here.
class Contact(models.Model):

    name=models.CharField(max_length=122)
    email=models.CharField(max_length=1222)
    phone=models.CharField(max_length=122)
    desc=models.TextField(max_length=12)
    date=models.DateField()


class Service(models.Model):
    s_name=models.CharField(max_length=50)
    s_desc=models.TextField(max_length=112)
    s_icon=models.CharField(max_length=50)