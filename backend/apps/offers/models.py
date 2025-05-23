from apps.ads.models import Ads
from apps.users.models import User
from django.db import models


class Offer(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает"),
        ("accepted", "Принята"),
        ("declined", "Отклонена"),
    ]
    user_sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_offers"
    )
    user_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_offers"
    )
    ad_sender = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="sent_proposals"
    )
    ad_receiver = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="received_proposals"
    )
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad_sender} → {self.ad_receiver} [{self.status}]"

    class Meta:
        db_table = "offers"
