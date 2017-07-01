from django.db import models
from djrichtextfield.models import RichTextField


# Create your models here.

class Experience(models.Model):

    title = models.CharField(max_length=70, null=True, blank=True)
    name = models.CharField(max_length=70, null=True, blank=True)
    site = models.CharField(max_length=70, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    fromdate = models.CharField(max_length=70, null=True, blank=True)
    todate = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.title


class About(models.Model):

    title = models.CharField(max_length=70, null=True, blank=True)
    image = models.CharField(max_length=70, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True)
    name = models.CharField(max_length=70, null=True, blank=True)
    site = models.CharField(max_length=70, null=True, blank=True)
    progrress = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.title

class Skills(models.Model):
    SKILL_CHOICES = (
        ('Language', 'LANGUGE'),
        ('Programming language', 'PROGRAMMING LANGUGE'),
        ('Self taught', 'SELFTOUGHT'),
        ('Software framework', 'FRAMEWORKS'),
        ('Other', 'OTHER'),
    )
    SKILL_GRADE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    PRIORITY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    type = models.CharField(max_length=70, choices=SKILL_CHOICES, null=True, blank=True)
    grade = models.CharField(max_length=70, choices=SKILL_GRADE, null=True, blank=True)
    priority = models.CharField(max_length=70, choices=PRIORITY, null=True, blank=True)
    name = models.CharField(max_length=70, null=True, blank=True)
    img = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
