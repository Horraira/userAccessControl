from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    nid = models.CharField(max_length=200, null=True)
    email= models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    bdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)


class Doctor(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    nid = models.CharField(max_length=200, null=True)
    email= models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    bdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)


class Pharmacy(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    pharmacy_reg_no = models.CharField(max_length=200, null=True)
    email= models.EmailField(blank=True, default="")
    password = models.CharField(max_length=200)
    conpassword = models.CharField(max_length=200)
    patient_address = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    bdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)
