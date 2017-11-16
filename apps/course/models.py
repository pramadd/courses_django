from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['name']) < 5 :
            errors['name'] = "name must be atleast 5 charactyers"
        if len(postData['desc']) < 3:
            errors['desc']  = "Description should be atleast 3 characters"
            print 'validating desc'
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

    def __repr__(self):
        return "User: \n{}\n{}\n".format(self.name, self.desc)
    
