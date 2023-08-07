from django.db import models

from django.urls import reverse
gender=(
    ("","Select Gender"),
    ("MALE","MALE"),
    ("FEMALE","FEMALE")
)

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30)
    sage=models.IntegerField()
    sgender=models.CharField(max_length=40,choices=gender)
    semail=models.EmailField(max_length=60)
    sphone=models.CharField(max_length=10)
    saddress=models.TextField()
    simage=models.ImageField(upload_to='student')

    def __str__(self):
        return self.sname
    
    def get_absolute_url(self):
        return reverse('StudentUpdateview', kwargs={'id': self.id})
    
    def delete_url(self):
        return reverse('StudentDeleteView', kwargs={'id': self.id})
    
    
    
   
    