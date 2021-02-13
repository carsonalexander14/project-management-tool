from django.db import models
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
    points = models.DecimalField(max_digits=999999999, decimal_places=2, default=0, blank=True, null=True)
    positions = models.ManyToManyField('Position', related_name="projects")
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

    STATUS_CHOICES = [
        ('A', 'Accepted'),
        ('R', 'Rejected'),
        ('P', 'Pending'),
        ('O', 'Open'),
    ] 

    project_master = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="position_set", null=True)
    position_title = models.CharField(max_length=15)
    position_description = models.CharField(max_length=150)
    skills = models.ManyToManyField('accounts.Skill')
    application_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')

    class Meta:
        ordering = ['position_title']

    def __str__(self):
        return self.position_title
        
""" 

 class ApplicationList(models.Model):


    acceptor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="acceptor")
    applications_list = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="applications_list")
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name="applications")


    class Meta:
        unique_together = ['acceptor', 'position']

    def __str__(self):
        return self.user.username

change user to position
    def add_application(self, user):
        if not user in self.applications_list.all():
            self.applications_list.add(user)
            self.save()

change user to position
    def remove_application(self, user):
        if user in self.applications_list.all():
            self.friends.remove(user)

    def remove_application_initiate(self, removee):
        remover_applications_list = self
        remover_applications_list.remove.application(removee)

        acceptor_list = Application.objects.get(user=removee)
        acceptor_list.remove_application(self.user)

class ApplicationRequest(models.Model):

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        receiver_application_list = ApplicationList.objects.get(user=self.receiver)

        if receiver_application_list:
            receiver_application_list.add_friend(self.sender)
            sender_application_list = ApplicationList.objects.get(user=self.sender)
            if sender_application_list:
                sender_application_list.add_application(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save() """