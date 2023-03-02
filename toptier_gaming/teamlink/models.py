from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TeamPost.Status.PUBLISHED)


class TeamPost(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', "Draft"
        PUBLISHED = 'PU', 'Published'
        
    class Visibility(models.TextChoices):
        ORG = "OR", "Org Internal"
        ROSTER = "RO", "Roster Internal"
        PUBLIC = "PU", "Publically Visible"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="team_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    visibility = models.CharField(max_length=2, choices=Visibility.choices, default=Visibility.PUBLIC)
    objects = models.Manager()
    published = PublishedManager() 
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
