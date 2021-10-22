from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="profile")
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    subject= models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name="teachers")


    def __str__(self):
        return self.user

class Day(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="groups")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.ManyToManyField(Day)
    start = models.TimeField()
    finish = models.TimeField()

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS_CHOICES = (("waiting", "Waiting"), ("active", "Active"))
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="waiting")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")

    def __str__(self):
        return self.name




