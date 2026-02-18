from django.db import models

# Create your models here.
from django.conf import settings
from apps.clients.models import Client


class Lead(models.Model):
    STATUS_NEW = 'new'
    STATUS_CONTACTED = 'contacted'
    STATUS_WON = 'won'
    STATUS_LOST = 'lost'

    STATUS_CHOICES = (
        (STATUS_NEW, 'New'),
        (STATUS_CONTACTED, 'Contacted'),
        (STATUS_WON, 'Won'),
        (STATUS_LOST, 'Lost'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_leads'
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_leads'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
