from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from decimal import Decimal

from accounts.models import User, Skill

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True)
    description = models.CharField(max_length=150)
    timeline = models.CharField(max_length=30)
    requirements = models.CharField(max_length=150)
    date_created = models.DateTimeField(default=timezone.now)
    positions = models.ManyToManyField(
        "Position",
        through='ProjectPosition',
        db_table='project_positions',
        related_name='projects',
        through_fields=('project', 'position'),
    )
    count = models.IntegerField(null=True, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Position(models.Model):
    project_master = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="position_set", null=True)
    position_title = models.CharField(max_length=15)
    position_description = models.CharField(max_length=150)
    skills = models.ManyToManyField('accounts.Skill')

    class Meta:
        ordering = ['position_title']

    def __str__(self):
        return self.position_title


class Application(models.Model):

    ACCEPTED = 'A'
    REJECTED = 'R'
    PENDING = 'P'
    OPEN = 'O'

    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending'),
        (OPEN, 'Open'),
    ]    

    application_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')
    acceptor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


class ProjectPosition(models.Model):
    position = models.ForeignKey(Position)
    project = models.ForeignKey(Project)
    application = models.ForeignKey(Application)
    