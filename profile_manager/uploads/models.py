from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    firstname = models.CharField(max_length=255, blank=True)
    lastname = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    employee_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
