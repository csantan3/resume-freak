from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here


class EndUser(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    device_id = models.UUIDField(
        primary_key=True, blank=True, default=uuid.uuid4, editable=True)

    # Display  Name
    def __str__(self):
        if self.user is not None:
            return self.user.username
        else:
            return str(self.device_id)


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    profile = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Resume(models.Model):
    end_user = models.ForeignKey(
        EndUser, null=True, blank=True, on_delete=models.CASCADE)
    contact_info = models.OneToOneField(
        ContactInfo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.contact_info.first_name + '\'s resume'

    @property
    def educations(self):
        return Education.objects.filter(resume=self)

    @property
    def experiences(self):
        return Experience.objects.filter(resume=self)

    @property
    def projects(self):
        return Project.objects.filter(resume=self)

    @property
    def skills(self):
        return Skill.objects.filter(resume=self)

    @property
    def hobbies(self):
        return Hobby.objects.filter(resume=self)


class Education(models.Model):
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    gpa = models.DecimalField(
        decimal_places=3, max_digits=6, null=True, blank=True)

    # foreign key to a resume
    resume = models.ForeignKey(
        Resume, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.school


class Experience(models.Model):
    organization = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    responsibilities = models.CharField(max_length=255)

    # foreign key to a resume
    resume = models.ForeignKey(
        Resume, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.organization


class Project(models.Model):
    name = models.CharField(max_length=50)
    responsibilities = models.CharField(max_length=255)

    # foreign key to a resume
    resume = models.ForeignKey(
        Resume, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)

    # foreign key to a resume
    resume = models.ForeignKey(
        Resume, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=50)

    # foreign key to a resume
    resume = models.ForeignKey(
        Resume, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
