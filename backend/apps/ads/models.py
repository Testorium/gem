from apps.categories.models import Category
from apps.users.models import User
from django.db import models


class Ads(models.Model):

    CONDITION_CHOICES = [
        ("new", "новый"),
        ("used", "б/у"),
        ("not working", "не работает"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ads",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    condition = models.CharField(
        max_length=50,
        choices=CONDITION_CHOICES,
        default="new",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "ads"
