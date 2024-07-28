from django.db import models

# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.TextField()
    speciality = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name