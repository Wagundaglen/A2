from django.db import models
from django.contrib.auth.models import User

class Bank(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)  # Add these lines if address should be part of the model
    phone_number = models.CharField(max_length=20, null=True, blank=True)  # Add these lines if phone_number should be part of the model
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    transit_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    capacity = models.IntegerField()
    last_modified = models.DateTimeField(auto_now=True)
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.bank.name}"



