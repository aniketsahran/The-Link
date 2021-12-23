from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import files


class CustomUser(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    roll_no = models.CharField('roll number', max_length=12, blank=True)
    faculty_code = models.CharField('faculty code', max_length=12, blank=True)


class Resource(models.Model):
    subject_code = models.CharField(max_length=10)
    year = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    material = models.FileField(upload_to='resources/%Y/%m/%d/%H-%M-%S')
    isApproved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='notifications/%Y/%m/%d/%H-%M-%S', blank=True, null=True)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Doubt(models.Model):
    asked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='asked_by')
    subject_code = models.CharField(max_length=10)
    faculty = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='faculty')
    doubt = models.TextField()
    file = models.FileField(upload_to='doubts/%Y/%m/%d/%H-%M-%S', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Solution(models.Model):
    doubt = models.ForeignKey(Doubt, on_delete=models.CASCADE)
    solution = models.TextField()
    file = models.FileField(upload_to='solutions/%Y/%m/%d/%H-%M-%S', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
