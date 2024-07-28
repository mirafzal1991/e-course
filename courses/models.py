from django.db import models
from teachers.models import Teacher

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    video = models.FileField(upload_to='media/courses')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)