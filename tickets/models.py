from django.db import models
from django.utils.text import slugify


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('REVIEW', 'In Review'),
        ('CLOSED', 'Closed'),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    creator = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @classmethod
    def get_by_title(cls, title):
        return cls.objects.filter(title=title)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Ticket, self).save(*args, **kwargs)