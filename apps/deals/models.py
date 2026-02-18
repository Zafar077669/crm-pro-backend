from django.db import models

# Create your models here.
from django.conf import settings
from apps.leads.models import Lead


class Deal(models.Model):
    STAGE_NEW = 'new'
    STAGE_NEGOTIATION = 'negotiation'
    STAGE_WON = 'won'
    STAGE_LOST = 'lost'

    STAGE_CHOICES = (
        (STAGE_NEW, 'New'),
        (STAGE_NEGOTIATION, 'Negotiation'),
        (STAGE_WON, 'Won'),
        (STAGE_LOST, 'Lost'),
    )

    lead = models.OneToOneField(
        Lead,
        on_delete=models.CASCADE,
        related_name='deal'
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='deals'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default='USD'
    )

    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default=STAGE_NEW
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Deal #{self.id} - {self.amount} {self.currency}"
