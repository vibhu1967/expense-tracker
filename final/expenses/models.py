
from datetime import date
from email.policy import default
from django.db import models

# Create your models here.


def upload_path(instance, filename):
    return '/'.join(['images', filename])


class Expenses(models.Model):
    category = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    amount = models.IntegerField()
    comments = models.CharField(null=True, max_length=50)
    approval_status = models.CharField(max_length=50, default="Pending")
    image = models.ImageField(null=True, upload_to=upload_path)
    approved_by = models.CharField(max_length=50, default="pending")
