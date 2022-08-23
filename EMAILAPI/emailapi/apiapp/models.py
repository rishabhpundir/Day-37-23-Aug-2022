from django.db import models

# Create your models here.

class Mail(models.Model):
    to_address = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.to_address