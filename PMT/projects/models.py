from django.db import models
from django.utils import timezone
from django.conf import settings

from accounts.models import User

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    timeline = models.CharField(max_length=30)
    requirements = models.CharField(max_length=150)
    end_date = models.DateField()
    date_created = models.DateTimeField(default=timezone.now)
    positions = models.ManyToManyField('Position', related_name="projects")

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    related_skill = models.CharField(max_length=15)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Application(models.Model):

    STATUS_CHOICES = [
        ('ACCEPTED', 'Accepted'),
        ('DENIED', 'Denied'),
        ('UNDECIDED', 'Undecided'),
    ]

    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='UNDECIDED',
    )

    class Meta:
        unique_together = ['applicant', 'position']

    def __str__(self):
        return "{}'s application to the {} position.".format(self.applicant, self.position)
    